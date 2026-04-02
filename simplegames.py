import random

def guess_the_number():
    number = random.randint(7, 978)
    print("\n=== Guess the Number ===")
    print("ykw i'm thinking of a number between 7 and 978.")
    
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if guess < number:
            print("Too low, you gotta try again!")
        elif guess > number:
            print("Too high, you gotta try again!")
        else:
            print("Correct! You win!")
            break

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("\n=== Rock, Paper, Scissors ===")
    
    while True:
        user_choice = input("Choose either rock, paper, or scissors (or 'quit' to go back): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in options:
            print("Invalid choice!")
            continue

        ai_choice = random.choice(options)
        print(f"AI chose: {ai_choice}")

        if user_choice == ai_choice:
            print("Tie!")
        elif (
            (user_choice == "rock" and ai_choice == "scissors") or
            (user_choice == "paper" and ai_choice == "rock") or
            (user_choice == "scissors" and ai_choice == "paper")
        ):
            print("You win, YAY!")
        else:
            print("You lose, BOOO!")

def main_menu():
    while True:
        print("\n=== Mini Games Menu ===")
        print("1) Guess the Number")
        print("2) Rock, Paper, Scissors")
        print("3) Quit")

        choice = input("Pick a game (1-3): ")
        if choice == "1":
            guess_the_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection!")

# Starting the program
main_menu()
