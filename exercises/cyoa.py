"""My first open-ended programming assignment, in which I create a game of choice!"""

import random

player: str = ""
points: int = 0

def greet() -> None:
    print("Welcome to the coinflip game.")
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}. In this game you will pick either heads or tails each round and see how many times you can consistently guess correctly. Your amount of points will increase by 1 each time you guess the coin flip correctly.")


def end_game() -> None:
    print(f"Your final score for number of times guesssed correctly in a row is {points}! Goodbye, {player}. ")
    quit()


def bonus_round() -> None:
    guess: int = input("Pick a number between 1 and 10 to earn an extra 10 points: ")
    random_int: int = random.randint(1,10)
    if guess == random_int:
        global points
        points += 10
        print("Congratulations, you received 10 bonus points.")
    else:
        print("You did not receive bonus points.")


def check_guess(x: int) -> int:
    # takes a random number and converts such to heads or tails
    # 0 is heads and 1 is tails
    random_int: int = random.randint(0,1)
    if random_int == x:
        # function returns 2, which specifies that the user guessed correctly.
        return 2
    else:
        return 3 # function returns 3, which specifies that the user guessed incorrectly.


def main() -> None:
    greet()
    global points
    user_guess: int = 0
    heads_or_tails: int = 0
    while user_guess < 2:
        user_guess = int(input("Enter 0 for heads, 1 for tails, or 2 to end the coin flip game. "))
        heads_or_tails = check_guess(user_guess)
        if heads_or_tails == 2:
            points += 1
            print("Congratulations, you guessed correctly so you gained 1 point!")
        if heads_or_tails == 3:
            print("Sorry, that was incorrect.")
            end_game()



if __name__ == "__main__":
    main()