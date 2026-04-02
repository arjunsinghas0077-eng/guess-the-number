import random

number = random.randint(1, 10)
guess = None

print("Guess the number between 1 and 10!")

while guess != number:
    try:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You win!")
    except ValueError:
        print("Please enter a valid number!")