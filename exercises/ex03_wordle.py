"""My EX03, where I create a structured wordle game."""
__author__ = "730604478"


def contains_char(str_to_search: str, guess_char: str) -> bool:  # This is where we declare the function that will be used in the main function to determine if characters at certain indices in a str match that of a single character str at some point.
    """Function for finding a character within another string."""
    assert len(guess_char) == 1
    str_index: int = 0
    while str_index < len(str_to_search):
        if str_to_search[str_index] == guess_char:
            return True
        else: 
            str_index += 1
    return False


def emojified(guess: str, secret: str) -> str:  # This is where we declare the function that will be used in the main function to be able to keep track of codes for the different colored emoji boxes and assign them for different indices of the guessed word, depending on if they match with any characters on any indices for the secret word.
    """Function for codifying str of emoji boxes."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    codify_index: int = 0
    codify_str: str = ""
    while codify_index < len(guess):
        if guess[codify_index] == secret[codify_index]:
            codify_str += GREEN_BOX
        else:
            if contains_char(secret, guess[codify_index]):
                codify_str += YELLOW_BOX
            else:
                codify_str += WHITE_BOX
        codify_index += 1
    return codify_str


def input_guess(expected_length: int) -> str:  # This is where we declare the function that will be used in the main function to keep prompting a user for a guess, until they input a guess that is the same length as the secret word (aka proper/expected length).
    """Function for asking user for guess."""
    user_guess: str = ""
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:  # This is where we declare the main function, which allows us to our "building block" functions into one function that has the power to implement high-level logic of the structured wordle game!
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    input_str: str = ""
    emojified_str: str = ""
    N: int = 1
    win: bool = False
    while N < 7 and win is False:
        print(f"=== Turn {N}/6 ===")
        input_str = input_guess(len(secret_word))
        emojified_str = emojified(input_str, secret_word)
        print(emojified_str)
        if input_str == secret_word:
            win = True
        else:
            N += 1
    if win:
        print(f"You won in {N}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":  # This is where we add a line of code that will make it possible for modules to import the functions created in this python program and reuse them.
    main()