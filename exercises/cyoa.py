"""My first open-ended programming assignment, in which I create a fun coinflip game!"""
__author__ = "730604478"

import random

player: str = ""
points: int = 0
SMILE_FACE: str = "\U0001F604"
SAD_FACE: str = "\U0001F622"


def greet() -> None:
    """The greet function welcomes the user, briefly explains the coinflip game rules, and prompts the user for a player name which will be stored in globals."""
    print("Welcome to the coinflip game.")
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}. In this game you will pick either heads or tails each round and see how many times you can consistently guess correctly. If you would like to end the game early, enter 2 for a given guess prompt. Your amount of points will increase by 1 each time you guess the coin flip correctly and you can receive bonus points with certain questions.")


def end_game() -> None:
    """The end_game function allows the player to view their final score (# of rounds successfully guessed correctly) before exiting the game."""
    print(f"Your final score is {points}! Goodbye, {player}. ")
    quit()


def bonus_round() -> None:
    """The bonus_round function prompts the user to answer an additional guessing question to possibly receive an extra 10 points. As menioned in the main function, thsi will only happen once user's current points is at 0."""
    guess: int = int(input("Pick a number between 1 and 10 to earn an extra 10 points: "))
    random_int: int = random.randint(1, 10)
    if guess == random_int:
        global points
        points += 10
        print(f"Congratulations, you received 10 bonus points. {SMILE_FACE} ")
    else:
        print(f"You did not receive bonus points. {SAD_FACE} ")


def check_guess(x: int) -> int:
    """The check_guess function uses a random of integer of either 0 or 1 to represent heads or tails. When the user's guess of 0 or 1 is passed to this function, it will return 2 (which represents correct guess) or 3 (which represents false guess)."""
    # takes a random number and converts such to heads or tails
    # 0 is heads and 1 is tails
    random_int: int = random.randint(0, 1)
    if random_int == x:
        # function returns 2, which specifies that the user guessed correctly.
        return 2
    else:
        return 3  # function returns 3, which specifies that the user guessed incorrectly.


def big_bonus(x: int) -> int:
    """The big_bonus function prompts the user to answer an addiitonal guessing question when current points is equal to 3. If answered correctly, the user's points increases by 20."""
    if x == 3:
        color_guess: str = input("What is my favorite color? ")
        if color_guess == "blue":
            print(f"Wow, {player}, You are a mind reader! You just earned 20 additional points! {SMILE_FACE} ")
            x += 20
        else:
            print(f"Sorry, that's wrong. {SAD_FACE} ")
    return x


def main() -> None:
    """The main function handles the game loop and makes the process of acccessing branches of the game and calling needed functions more efficient."""
    greet()
    global points
    user_guess: int = 0
    heads_or_tails: int = 0
    while user_guess < 2:  # this is where the game loop begins, in which as long as user's guess is 0 (heads) or 1 (tails), the loop will run.
        points = big_bonus(points)  # here we call the 20-point bonus function and will add 20 to points' value.
        if points == 1:
            bonus_round()  # here we call the 10-point bonus function and will add 10 to points' value when points currently equals 1 before entering such function.
        user_guess = int(input("Enter 0 for heads, 1 for tails, or 2 to end the coin flip game. "))
        if user_guess == 2:
            end_game()
        heads_or_tails = check_guess(user_guess)  # on the following lines we use a variable (heads_or_tails) to keep track of if the user guessed correctly (2) or incorrectly (3) so that the correct output message can be sent and points are correctly updated.
        if heads_or_tails == 2:
            points += 1
            print(f"Congratulations, you guessed correctly so you gained 1 point! {SMILE_FACE} ")
        if heads_or_tails == 3:
            print(f"Sorry, that was incorrect. {SAD_FACE} ")
            end_game()


if __name__ == "__main__":
    main()