import random

def hit():
    """Give the player another card"""
    return random.randint(1,11)

def result(player_hand, house_hand):
    if sum(player_hand) == 21 and sum(house_hand) == 21:
        return "push"
    elif sum(player_hand) > 21:
        return "bust"
    elif sum(player_hand) == 21:
        return "blackjack"
    elif sum(player_hand) > sum(house_hand):
        return "win"
    else:
        return "lose"