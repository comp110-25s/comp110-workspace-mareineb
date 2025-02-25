"""Attempting Wordle in COMP110!"""

__author__: str = "730611339"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_word: str, searched_character: str) -> bool:
    """Searches if a word's character is found in the secret word!"""
    assert len(searched_character) == 1, f"len('{searched_character}') is not 1"
    idx: int = 0
    while idx < len(search_word):
        if search_word[idx] == searched_character:
            return True
        else:
            idx = idx + 1
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """Codifies guesses into green, white, and yellow emojis!"""
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"
    idx: int = 0
    emojified_result: str = ""
    while idx < len(guessed_word):
        if guessed_word[idx] == secret_word[idx]:
            emojified_result = emojified_result + GREEN_BOX
            idx += 1
        elif contains_char(secret_word, guessed_word[idx]):
            emojified_result = emojified_result + YELLOW_BOX
            idx += 1
        else:
            emojified_result = emojified_result + WHITE_BOX
            idx += 1
    return emojified_result


def input_guess(required_word_length: int) -> str:
    """Checks to see if the guessed_word is at a specific character length."""
    guessed_word: str = input(f"Enter a {required_word_length} character word:")
    while len(guessed_word) != required_word_length:
        guessed_word = input(f"That wasn't {required_word_length} chars! Try again:")
    return guessed_word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    guessed_word: str = ""
    secret_length: int = len(secret)
    while turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        guessed_word = input_guess(secret_length)
        print(emojified(guessed_word, secret))
        if guessed_word == secret:
            print(f"You won in {turn_number}/6 turns!")
            return None
        else:
            turn_number += 1
            if turn_number == 7:
                print("X/6 - Sorry, try again tomorrow!")
                return None


if __name__ == "__main__":
    main(secret="codes")
