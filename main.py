print("WELCOME TO HIGHER LOWER GAME!!!!")
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
   
    return f"{account_name}, a {account_descr}"

def check_answer(user_guess, a_followers, b_followers):

    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
score = 0
game_conti = True
account_b = random.choice(data)

while game_conti:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")

    print("VS")

    print(f"Against B : {format_data(account_b)}")


    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    a_follower = account_a["followers"]
    b_follower = account_b["followers"]

    is_correct = check_answer(guess , a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"you are right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score:{score}")
        game_conti = False