from game_data import data
from art import vs, logo
import random

print(logo)
def get_random_data():
    person=random.choice(data)
    return person

def compare(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return account1
    else:
        return account2

def compare_user_input(account, accountX, current_score):
    if account==accountX:
        current_score+=1
    return current_score
        


account1=get_random_data()
player_right =True
current_score=0

while player_right == True:
    account2=get_random_data()
    print(f"Compare A: {account1['name']}, {account1['description']}, from {account1['country']}")
    print(vs)
    print(f"Against B: {account2['name']}, {account2['description']}, from {account2['country']}")
    account=compare(account1, account2)
    input_account=input("Who has more followers? Type 'A' or 'B': ")
    if input_account=='A':
        new_score=compare_user_input(account, account1, current_score)
        if new_score !=current_score:
            current_score=new_score
            print(f"You're Right!! A is Big. Your score is {current_score}")
        else:
            print(f"You're Wrong. Your final score {current_score}")
            player_right=False
    else:
        new_score=compare_user_input(account, account2, current_score)
        if new_score !=current_score:
            current_score=new_score
            print(f"You're Right!! B is Big. Your score is {current_score}")
            account1=account
        else:
            print(f"You're Wrong. Your final score {current_score}")
            player_right=False
    
 




