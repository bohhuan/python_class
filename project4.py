"""
game: rock, paper and scissors
"""
import random

def lets_play():
    
    your_choice = input("what is your choice ? 'r' for rock, 'p' for paper, 's' for scissors")
    computer_choice = random.choice(['r', 'p', 's'])
    
    if your_choice == computer_choice:
        return 'it is a tie'

    if are_you_win(your_choice, computer_choice):
        return "you won !"
    
    return "you lost !"

    
def are_you_win(your_choice, computer_choice):
    """
    return True if your_choice wins computer_choice. follow the rules: 
    rock > scissors,  scissors > paper, paper > rock. i.e, r > s, s > p, p > r
    """


print(lets_play())