from game_data import data
import art
from random import choice
import os


def clear(): return os.system('cls')


print(art.logo)


def dictionary_cleaner(account):
    name = account['name']
    follower_count = account['follower_count']
    description = account['description']
    country = account['country']
    a = (f"{name}, the {description}, from {country}")
    return follower_count, a


def answer_checker(answer, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        winner = 'A'
    else:
        winner = 'B'
    if winner == answer:
        return True
    else:
        return False


a_account = choice(data)
b_account = choice(data)
while a_account == b_account:
    b_account = choice(data)
a_follower_count, a_candidate_description = dictionary_cleaner(a_account)
b_follower_count, b_candidate_description = dictionary_cleaner(b_account)
print(a_follower_count)
print(b_follower_count)


score = 0
should_finish = False
while should_finish == False:
    print(f"Compare A: {a_candidate_description}")
    print(art.vs)
    print(f"Against B: {b_candidate_description}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    print(art.logo)
    result = answer_checker(answer, a_follower_count, b_follower_count)
    print(result)
    if result:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"You are wrong! Current score: {score}")
        should_finish = True
    a_candidate_description = b_candidate_description
    b_account = choice(data)
    while a_account == b_account:
        b_account = choice(data)
    b_follower_count, b_candidate_description = dictionary_cleaner(b_account)
