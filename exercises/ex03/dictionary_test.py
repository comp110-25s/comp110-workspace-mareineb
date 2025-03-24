"""Contains unit tests for the dictionary module to check for validation!"""

__author__: str = "730611339"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use1() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use2() -> None:
    assert invert({"apple": "banana", "cherry": "dragonfruit"}) == {
        "banana": "apple",
        "dragonfruit": "cherry",
    }


def test_invert_edge() -> None:
    assert invert({}) == {}


def test_count_use1() -> None:
    assert count(["pink", "blue", "green", "blue", "red"]) == {
        "pink": 1,
        "blue": 2,
        "green": 1,
        "red": 1,
    }


def test_count_use2() -> None:
    assert count(["a", "b", "c", "a", "b", "a", "a"]) == {"a": 4, "b": 2, "c": 1}


def test_count_edge() -> None:
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    assert (
        favorite_color(
            {
                "Xander": "black",
                "Morgan": "blue",
                "Mari": "green",
                "Alexandria": "purple",
                "Sam": "purple",
            }
        )
        == "purple"
    )


def test_favorite_color_use2() -> None:
    assert (
        favorite_color(
            {
                "Angie": "purple",
                "Rebekah": "purple",
                "Lufei": "blue",
                "KC": "red",
                "Catherine": "blue",
            }
        )
        == "purple"
    )


def test_favorite_color_edge1() -> None:
    assert favorite_color({}) == None


def test_favorite_color_edge2() -> None:
    assert (
        favorite_color(
            {
                "Xander": "black",
                "Morgan": "blue",
                "Mari": "green",
                "Alexandria": "purple",
            }
        )
        == "black"
    )


def test_bin_len_use1() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge() -> None:
    if bin_len([""]) == None:
        return False
