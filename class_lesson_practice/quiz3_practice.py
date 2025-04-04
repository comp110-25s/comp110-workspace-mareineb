def survivor(votes: list[str]) -> str:
    """Pick whoever has the most votes to kick them off."""
    largest_count: int = 0
    dict_frq: dict[str, int] = {}
    for name in votes:
        if name not in dict_frq:
            dict_frq[name] = 1
        elif name in dict_frq:
            dict_frq[name] += 1
    for name in dict_frq:
        if dict_frq[name] > largest_count:
            largest_count = dict_frq[name]
    for name in dict_frq:
        if dict_frq[name] == largest_count:
            return name
