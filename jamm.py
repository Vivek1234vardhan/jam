import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
