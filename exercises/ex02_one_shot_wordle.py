"""My EX02, where I create a one-shot wordle game."""
__author__ = "730604478"


secret_word: str = "python"  # here we are initializing what the secret word is. Whatever is inside of the quotes will be our secret word, and its length will be used in the input prompt as a str.

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

user_guess: str = input(f"What is your { len(secret_word) }-letter guess? ")

guess_index: int = 0   # here we initialize the index of the user's guessed word to 0
guess_emojibox: str = ""


while len(user_guess) != len(secret_word):  # here we see our first loop in the program, in which the loop will continue unless the user inputs a word that is the same length as the secret.
    new_input: str = input(f"That was not { len(secret_word) } letters! Try again: ")
    user_guess = new_input  # it's important that we redefine the user's guessed word to the new input, so that the computer knows whether to run the loop again.

if user_guess != secret_word:  # here is where we will later begin another loop if the user's guess is not exactly the secret, based on more conditions below.
    while guess_index < len(user_guess):  # here we will begin the second loop in the program, only if the user's guess' length is less than that of the secret.
        if user_guess[guess_index] == secret_word[guess_index]:
            guess_emojibox = guess_emojibox + GREEN_BOX
            guess_index += 1 
        else:  # if the index of the user's guess does not equal that of the secret word, we instead now initialize a variable to keep track of if any matches are at other indices.
            elsewhere: bool = False
            alternate_indices: int = 0  # here is another variable we initialize, so that we can keep track of how many alternate indices we could test 
            while not elsewhere and alternate_indices < len(secret_word):  # here is the third loop in our program, which begins when elsewhere is not true and the alternate indices remaining is less than the length of the secret.
                if user_guess[guess_index] == secret_word[alternate_indices]:
                    elsewhere = True
                else:  # if the index of the user's guess does not equal the alternate index of the secret, we will then add 1 to the alternate indices.
                    alternate_indices += 1
            guess_index += 1  # once the loop above completes and no more indices remain to check, we add 1 to the index of the guess. 
            if elsewhere:
                guess_emojibox = guess_emojibox + YELLOW_BOX  # this is how we tell the computer to print yellow boxes at the indices where guessed letters are in the secret, but at different locations.
            else:
                guess_emojibox = guess_emojibox + WHITE_BOX  # this is how we tell the computer to print yellow boxes at the indices where guessed letters are not in the secret at all.

    print(guess_emojibox)  # this is where the computer then prints however many boxes that are the length of the secret word, varying in color(aka emoji box) based on if letters are in correct position, should be at other position, or not in secret word at all.
    print("Not quite. Play again soon!")


if user_guess == secret_word:  # this if statement is used when the user's guess is actually exactly the secret word, therefore we could just print all green boxes. 
    while guess_index < len(secret_word):
        if user_guess[guess_index] == secret_word[guess_index]:
            guess_emojibox = guess_emojibox + GREEN_BOX
        guess_index += 1
    print(guess_emojibox)
    print("Woo! You got it!")