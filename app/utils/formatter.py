def money(x):

    if x >= 1_000_000:
        return f"₹{x/1_000_000:.2f} M"

    if x >= 1000:
        return f"₹{x/1000:.2f} K"

    return f"₹{x:.2f}"


def number(x):
    return f"{int(x):,}"