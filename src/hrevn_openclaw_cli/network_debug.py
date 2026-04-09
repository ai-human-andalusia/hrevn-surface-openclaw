#!/usr/bin/env python3
"""Minimal network diagnostic for the OpenClaw HREVN surface."""

from __future__ import annotations

import argparse
import json
import socket
import ssl
import sys
import traceback
import urllib.error
import urllib.parse
import urllib.request

from .cli import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, env_or_default


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Debug HREVN OpenClaw network calls.")
    parser.add_argument(
        "--base-url",
        default=env_or_default("HREVN_API_BASE_URL", DEFAULT_BASE_URL),
        help="Managed API base URL.",
    )
    parser.add_argument(
        "--api-key",
        default=env_or_default("HREVN_API_KEY"),
        help="API key for POST /v1/baseline-check. Defaults to HREVN_API_KEY.",
    )
    return parser.parse_args()


def print_header(title: str) -> None:
    print(f"\n=== {title} ===")


def show_json(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=True))


def main() -> int:
    args = parse_args()
    parsed = urllib.parse.urlparse(args.base_url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)

    if parsed.scheme not in {"http", "https"} or not host:
        print(f"Invalid base URL: {args.base_url!r}", file=sys.stderr)
        return 2

    print_header("Environment")
    show_json(
        {
            "python": sys.version.split()[0],
            "openssl": ssl.OPENSSL_VERSION,
            "base_url": args.base_url,
            "host": host,
            "port": port,
            "has_api_key": bool(args.api_key),
        }
    )

    print_header("DNS")
    try:
        infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        simplified = []
        for family, socktype, proto, canonname, sockaddr in infos:
            simplified.append(
                {
                    "family": family,
                    "socktype": socktype,
                    "proto": proto,
                    "sockaddr": list(sockaddr) if isinstance(sockaddr, tuple) else sockaddr,
                }
            )
        show_json(simplified)
    except Exception as exc:
        print(f"DNS failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1

    print_header("TCP")
    try:
        with socket.create_connection((host, port), timeout=DEFAULT_TIMEOUT):
            print("tcp_connect: ok")
    except Exception as exc:
        print(f"TCP failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1

    print_header("GET /v1/health")
    try:
        with urllib.request.urlopen(f"{args.base_url.rstrip('/')}/v1/health", timeout=DEFAULT_TIMEOUT) as response:
            payload = json.loads(response.read().decode("utf-8"))
            show_json({"status_code": response.status, "payload": payload})
    except Exception as exc:
        print(f"GET /v1/health failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1

    if not args.api_key:
        print_header("POST /v1/baseline-check")
        print("Skipped because no API key was provided.")
        return 0

    print_header("POST /v1/baseline-check")
    payload = {
        "task_type": "ai_workflow",
        "profile": "eu_readiness_profile",
        "record": {
            "human_oversight": {},
            "risk_register": {},
            "evidence_lifecycle": {},
        },
        "metadata": {
            "surface": "openclaw",
            "source": "network_debug",
        },
    }
    request = urllib.request.Request(
        f"{args.base_url.rstrip('/')}/v1/baseline-check",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {args.api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
            result = json.loads(response.read().decode("utf-8"))
            show_json({"status_code": response.status, "result": result})
            return 0
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"HTTPError: {exc.code}", file=sys.stderr)
        print(detail, file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"POST /v1/baseline-check failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
