import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess_input = input("Take a guess: ").strip()

    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct!!! You have found the number in {attempts} attempts!")
        break
