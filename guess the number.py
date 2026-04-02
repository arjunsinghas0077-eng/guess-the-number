import random

number = random.randint(10, 100)
guess = 77

print("Guess the number between 10 and 100!")

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
