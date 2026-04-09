#!/usr/bin/env python3
"""Compatibility wrapper for the installable OpenClaw CLI."""

from hrevn_openclaw_cli.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
