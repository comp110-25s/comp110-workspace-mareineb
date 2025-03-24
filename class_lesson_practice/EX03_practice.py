from exercises.ex03.dictionary import count


def favorite_color(ppl_fave_colors: dict[str, str]) -> str:
    """Gives the overall favorite color for most people in a dictionary."""
    list_of_colors: list[str] = []
    largest_count: int = 0
    for key in ppl_fave_colors:
        list_of_colors.append(ppl_fave_colors[key])
    frq_of_colors: dict[str, int] = count(list_of_colors)
    for key in frq_of_colors:
        if frq_of_colors[key] >= largest_count:
            largest_count = frq_of_colors[key]
    for key in frq_of_colors:
        if frq_of_colors[key] == largest_count:
            return key
