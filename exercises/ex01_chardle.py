"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730604478"

user_wordguess: str = input("Enter a 5-character word: ")
if len(user_wordguess) != 5:
    print("Error: Word must contain 5 characters")
    quit()

user_letterguess: str = input("Enter a single character: ")
if len(user_letterguess) != 1:
    print("Error: Character must be a single character.")
    quit()

user_instances: int = 0

print("Searching for " + user_letterguess + " in " + user_wordguess)


if user_letterguess == user_wordguess[0]:
    print(user_letterguess + " found at index 0")
    user_instances = user_instances + 1
if user_letterguess == user_wordguess[1]:
    print(user_letterguess + " found at index 1")
    user_instances = user_instances + 1
if user_letterguess == user_wordguess[2]:
    print(user_letterguess + " found at index 2")
    user_instances = user_instances + 1
if user_letterguess == user_wordguess[3]:
    print(user_letterguess + " found at index 3")
    user_instances = user_instances + 1
if user_letterguess == user_wordguess[4]:
    print(user_letterguess + " found at index 4")
    user_instances = user_instances + 1


if user_instances < 1:
    print("No instances of " + user_letterguess + " found in " + user_wordguess)
if user_instances == 1:
    print("1 instance of " + user_letterguess + " found in " + user_wordguess)
if user_instances > 1:
    print(str(user_instances) + " instances of " + user_letterguess + " found in " + user_wordguess)