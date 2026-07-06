from typing import Any


def format_currency(value: float) -> str:
    return f"${value:,.2f}"


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
