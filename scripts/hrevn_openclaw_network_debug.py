#!/usr/bin/env python3
"""Compatibility wrapper for the installable OpenClaw network debug CLI."""

from hrevn_openclaw_cli.network_debug import main


if __name__ == "__main__":
    raise SystemExit(main())
