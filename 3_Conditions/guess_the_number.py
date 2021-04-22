import random

# target is the number the player needs to guess
# the computer selects a random number from 1 to 99
target = random.choice(range(1, 100))

print("What number am I thinking of?")
tries = 0

# this loop will continue forever
while True:

    try:
        # first we get a guess from the player
        guess = int(input("\nGuess a number! (0-100)\n>>>"))
        # then we check if the guess is a legal guess
        if guess > 99 or guess < 1:
            # we raise an error if the player didn't follow the rules
            raise ValueError
    except ValueError:
        # if the error gets raised, we remind the player of the rules and start the loop again
        print('Please enter a number between 0 and 100\nOnly use integers!')
        continue
    if guess != target:
        # if guess is incorrect, tell the user to go bigger or smaller
        if target > guess:
            print("Bigger!\n")
        if target < guess:
            print("Smaller!\n")
    if guess == target:
        # guess is correct, tell the user they got it right!
        print('Winner!')
        print(f"You got it in {tries + 1} guesses!\n")
        # Since the player won, the game is over. We use the 'break' keyword to end the loop
        break
    # increase tries by one before starting the next loop to keep track of how many tries.
    tries += 1
