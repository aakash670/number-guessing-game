import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Make a guess: "))
        except ValueError:
            print("⛔ Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"😢 You've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
