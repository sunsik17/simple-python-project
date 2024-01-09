def get_id(link: str) -> str:
    return "".join([c for c in link if c.isdigit()])