def parse_price(price_text: str) -> int:
    """
    Convert price string like '50,999' into integer 50999.
    Removes commas, dots, and spaces.
    """
    return int(price_text.replace(",", "").replace(".", "").strip())

