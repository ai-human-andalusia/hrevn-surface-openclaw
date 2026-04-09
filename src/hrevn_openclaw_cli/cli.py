#!/usr/bin/env python3
"""Installable CLI bridge for the public HREVN managed API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_BASE_URL = "https://api.hrevn.com"
DEFAULT_TIMEOUT = 20
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASELINE_INPUT = REPO_ROOT / "examples" / "baseline_check_request.json"
DEFAULT_GOVERNANCE_GAP_INPUT = REPO_ROOT / "examples" / "governance_gap_request.json"


def env_or_default(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None:
        return default
    value = value.strip()
    return value or default


def normalize_base_url(value: str) -> str:
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit(f"Invalid HREVN_API_BASE_URL/base URL: {value!r}")
    return value.rstrip("/")


def require_key(value: str | None) -> str:
    if value:
        return value
    raise SystemExit("HREVN_API_KEY is required. Run `hrevn health-check` first if you only want connectivity.")


def read_json(path: str | Path) -> object:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def get_json(base_url: str, path: str) -> object:
    request = urllib.request.Request(f"{base_url}{path}")
    with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8"))


def post_json(base_url: str, api_key: str, path: str, payload: object) -> object:
    request = urllib.request.Request(
        f"{base_url}{path}",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8"))


def get_bytes(base_url: str, api_key: str, path: str) -> bytes:
    request = urllib.request.Request(
        f"{base_url}{path}",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return response.read()


def self_test_payload() -> object:
    return {
        "task_type": "ai_workflow",
        "profile": "eu_readiness_profile",
        "record": {
            "human_oversight": {},
            "risk_register": {},
            "evidence_lifecycle": {},
        },
        "metadata": {
            "surface": "openclaw",
            "source": "self_test",
        },
    }


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Call the HREVN managed API from OpenClaw.")
    root.add_argument(
        "--base-url",
        default=env_or_default("HREVN_API_BASE_URL", DEFAULT_BASE_URL),
        help="Managed API base URL.",
    )
    root.add_argument(
        "--api-key",
        default=env_or_default("HREVN_API_KEY"),
        help="API key. Defaults to HREVN_API_KEY.",
    )

    subparsers = root.add_subparsers(dest="command", required=True)

    subparsers.add_parser("health-check")
    subparsers.add_parser("self-test")
    subparsers.add_parser("baseline")
    subparsers.add_parser("governance-gap")

    baseline = subparsers.add_parser("baseline-check")
    baseline.add_argument("--input", required=True)

    generate = subparsers.add_parser("generate-bundle")
    generate.add_argument("--input", required=True)

    verify = subparsers.add_parser("verify-bundle")
    verify.add_argument("--source", required=True)

    download = subparsers.add_parser("download-bundle")
    download.add_argument("--bundle-id", required=True)
    download.add_argument("--output")

    return root


def print_json(data: object) -> None:
    print(json.dumps(data, indent=2))


def run_health_check(base_url: str) -> int:
    result = get_json(base_url, "/v1/health")
    print_json({"health_check": "ok", "base_url": base_url, "status": result.get("status")})
    return 0


def run_self_test(base_url: str, api_key: str) -> int:
    health = get_json(base_url, "/v1/health")
    result = post_json(base_url, api_key, "/v1/baseline-check", self_test_payload())
    print_json(
        {
            "self_test": "ok",
            "base_url": base_url,
            "health": health.get("status"),
            "auth": "ok",
            "baseline_result": result.get("result"),
            "profile_detected": result.get("profile_detected"),
            "readiness_level": result.get("readiness_level"),
            "check_id": result.get("check_id"),
            "checked_at": result.get("checked_at"),
        }
    )
    return 0


def run_baseline_from_file(base_url: str, api_key: str, path: str | Path) -> int:
    print_json(post_json(base_url, api_key, "/v1/baseline-check", read_json(path)))
    return 0


def run_generate_bundle(base_url: str, api_key: str, path: str) -> int:
    print_json(post_json(base_url, api_key, "/v1/generate-bundle", read_json(path)))
    return 0


def run_verify_bundle(base_url: str, api_key: str, source: str) -> int:
    print_json(post_json(base_url, api_key, "/v1/verify-bundle", {"source": source}))
    return 0


def run_download_bundle(base_url: str, api_key: str, bundle_id: str, output: str | None) -> int:
    bundle = get_bytes(base_url, api_key, f"/v1/bundles/{urllib.parse.quote(bundle_id)}/download")
    if output:
        Path(output).write_bytes(bundle)
        print(output)
    else:
        sys.stdout.buffer.write(bundle)
    return 0


def main() -> int:
    args = parser().parse_args()
    base_url = normalize_base_url(args.base_url)

    try:
        if args.command == "health-check":
            return run_health_check(base_url)
        if args.command == "self-test":
            return run_self_test(base_url, require_key(args.api_key))
        if args.command == "baseline":
            return run_baseline_from_file(base_url, require_key(args.api_key), DEFAULT_BASELINE_INPUT)
        if args.command == "governance-gap":
            return run_baseline_from_file(base_url, require_key(args.api_key), DEFAULT_GOVERNANCE_GAP_INPUT)
        if args.command == "baseline-check":
            return run_baseline_from_file(base_url, require_key(args.api_key), args.input)
        if args.command == "generate-bundle":
            return run_generate_bundle(base_url, require_key(args.api_key), args.input)
        if args.command == "verify-bundle":
            return run_verify_bundle(base_url, require_key(args.api_key), args.source)
        if args.command == "download-bundle":
            return run_download_bundle(base_url, require_key(args.api_key), args.bundle_id, args.output)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        if exc.code in {401, 403}:
            print(f"HREVN managed API authentication failed ({exc.code}): {detail}", file=sys.stderr)
        else:
            print(f"HREVN managed API error {exc.code}: {detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"HREVN managed API connection failed: {exc}", file=sys.stderr)
        return 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
