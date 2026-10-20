import random

print("Difficulty:\n" \
"1.Easy 1-50\n" \
"2.Medium 1-100\n" \
"3.Hard 1-500")

difficulty = int(input("Choose a diffculty between 1-3: "))

if difficulty == 1:
    lowest_number = 1
    highest_number = 50
elif difficulty == 2:
    lowest_number = 1
    highest_number = 100
elif difficulty == 3:
    lowest_number = 1
    highest_number = 500
    

guesses = 0

answer = random.randint(lowest_number, highest_number)

is_running = True

print("Number guessing game!")

while is_running:
    guess = input(f"Select a number between {lowest_number} and {highest_number}: ")

    if guess.isdigit():
        guess = int(guess)

        if guess < lowest_number or guess > highest_number:
            print("Invalid Number!")
        elif guess > answer:
            guesses += 1
            print("Too High!Try Again")
        elif guess < answer:
            guesses += 1
            print("Too low! Try again")
        else:
            guesses += 1
            print(f"You guessed the number correctly! The number was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Input!")
        