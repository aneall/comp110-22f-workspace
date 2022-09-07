"""My EX02, where I create a one-shot wordle game."""
__author__ = "730604478"

from operator import index

secret_word: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

user_guess: str = input("What is your 6-letter guess? ")



guess_index: int = 0
guess_emojibox: str = ""

while guess_index < len(secret_word):
    if user_guess[guess_index] == secret_word[guess_index]:
        guess_emojibox = GREEN_BOX
    else:
        guess_emojibox = WHITE_BOX
    guess_index += 1
print(guess_emojibox)


-------- ^^ practice for part 2


while len(user_guess) != len(secret_word):
    input("That was not 6 letters! Try again: ")
    user_guess = input("That was not 6 letters! Try again: ")

if user_guess != secret_word:
    while guess_index < len(secret_word):
        if user_guess[guess_index] == secret_word[guess_index]:
            guess_emojibox = GREEN_BOX
        else:
            guess_emojibox = WHITE_BOX
        guess_index += 1
    print(guess_emojibox)
    print("Not quite. Play again soon!")
    quit()


if user_guess == secret_word:
    while guess_index < len(secret_word):
        if user_guess[guess_index] == secret_word[guess_index]:
            guess_emojibox = GREEN_BOX
        else:
            guess_emojibox = WHITE_BOX
        guess_index += 1
    print(guess_emojibox)
    print("Woo! You got it!")
    quit()



----- ^ part 1 + part 2?




guess_index: str = user_guess[0]
guess_emojibox: str = ""

while len(guess_index) < len(secret_word):
    if guess_index == secret_word[0]:
        guess_emojibox = guess_emojibox + GREEN_BOX
    else: 
        guess_emojibox = guess_emojibox + WHITE_BOX
    guess_index = user_guess[1]
print(guess_emojibox)

--- part 2 old idea ^^