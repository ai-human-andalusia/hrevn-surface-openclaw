#!/usr/bin/env python3
"""OpenClaw-friendly CLI bridge for the public HREVN managed API."""

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


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Call the HREVN managed API from OpenClaw.")
    root.add_argument(
        "--base-url",
        default=os.environ.get("HREVN_API_BASE_URL", DEFAULT_BASE_URL),
        help="Managed API base URL.",
    )
    root.add_argument(
        "--api-key",
        default=os.environ.get("HREVN_API_KEY"),
        help="API key. Defaults to HREVN_API_KEY.",
    )

    subparsers = root.add_subparsers(dest="command", required=True)

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


def require_key(value: str | None) -> str:
    if value:
        return value
    raise SystemExit("HREVN_API_KEY is required")


def read_json(path: str) -> object:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def post_json(base_url: str, api_key: str, path: str, payload: object) -> object:
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}{path}",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def get_bytes(base_url: str, api_key: str, path: str) -> bytes:
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}{path}",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(request) as response:
        return response.read()


def main() -> int:
    args = parser().parse_args()
    api_key = require_key(args.api_key)

    try:
        if args.command == "baseline-check":
            print(
                json.dumps(
                    post_json(
                        args.base_url,
                        api_key,
                        "/v1/baseline-check",
                        read_json(args.input),
                    ),
                    indent=2,
                )
            )
            return 0

        if args.command == "generate-bundle":
            print(
                json.dumps(
                    post_json(
                        args.base_url,
                        api_key,
                        "/v1/generate-bundle",
                        read_json(args.input),
                    ),
                    indent=2,
                )
            )
            return 0

        if args.command == "verify-bundle":
            print(
                json.dumps(
                    post_json(
                        args.base_url,
                        api_key,
                        "/v1/verify-bundle",
                        {"source": args.source},
                    ),
                    indent=2,
                )
            )
            return 0

        if args.command == "download-bundle":
            bundle = get_bytes(
                args.base_url,
                api_key,
                f"/v1/bundles/{urllib.parse.quote(args.bundle_id)}/download",
            )
            if args.output:
                Path(args.output).write_bytes(bundle)
                print(args.output)
            else:
                sys.stdout.buffer.write(bundle)
            return 0

    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"HREVN managed API error {exc.code}: {detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"HREVN managed API connection failed: {exc}", file=sys.stderr)
        return 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
