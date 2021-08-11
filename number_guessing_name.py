import random

print("Welcome to the Number Guessing Name!")
print("I'm thinking of number between 1 and 100.")
should_continue = 'no'
while should_continue == 'no':
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        print("You have 10 attempts remaining to guess the number.")
        lives = 10
        should_continue = 'yes'
    elif difficulty == 'hard':
        print("You have 5 attempts remaining to guess the number.")
        lives = 5
        should_continue = 'yes'
    else:
        print('Input is wrong! Try again!')
        should_continue = 'no'

# Assigning random number to answer
answer = random.choice(range(1, 101))
# Game start
guess = 0


def attempts(lives):
    if guess != answer:
        lives -= 1
        print(f'You have {lives} attempts remaining!')
    else:
        print("Congrats!")
    return lives


def matching_answer(guess, answer):
    if guess > answer:
        print('Too high')
    elif guess < answer:
        print('Too low')
    else:
        print('You win!')


# Later change 'while loop to guess != answer'.
while guess != answer and lives > 0:
    guess = int(input("Make a guess: "))
    matching_answer(guess, answer)
    lives = attempts(lives)
