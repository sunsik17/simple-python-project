def get_id(link: str) -> str:
    result = []
    for c in link:
        if c.isdigit():
            result.append(c)

    return "".join(result)