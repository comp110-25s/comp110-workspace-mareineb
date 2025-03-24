"""Contains a dictionary to find certain values"""

__author__: str = "730611339"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts dictionary keys and values"""
    inverted_dict: dict[str, str] = {}
    input_value: str = ""
    for key in input_dict:
        input_value = input_dict[key]
        if input_value in inverted_dict:
            raise KeyError("Sorry, that key is already used!")
        else:
            inverted_dict[input_dict[key]] = key
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequencies of a str in a list"""
    count_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] in count_dict:
            count_dict[input_list[idx]] += 1
            idx += 1
        else:
            count_dict[input_list[idx]] = 1
            idx += 1
    return count_dict


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
            return f"{key}"


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    """Finds the lengths of certain words in a list and categorizes them."""
    idx: int = 0
    chara_len_dict: dict[int, set[str]] = {}
    set_w_len: set[str] = set()
    word_len: int = 0
    while idx < len(word_list):
        word_len = len(word_list[idx])
        if word_len in chara_len_dict and word_list[idx] != chara_len_dict[word_len]:
            set_w_len = chara_len_dict[word_len]
            set_w_len.add(word_list[idx])
            chara_len_dict[word_len] = set_w_len
            idx += 1
        elif word_len not in chara_len_dict:
            set_w_len = set()
            set_w_len.add(word_list[idx])
            chara_len_dict[word_len] = set_w_len
            idx += 1
    return chara_len_dict
