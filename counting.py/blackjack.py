# Game of Blackjack in Python

import random


from blackjack_functions import hit, result


def play_game():
    print("Welcome to Blackjack")
    print("Lets play best of 3")
    print("Good Luck ;)")
    total_hands = 0
    players_score = 0
    dealers_score = 0
    
    while total_hands < 3:

        print("Hand Number " + str(total_hands + 1) + ". Dealing the cards.")

        house_cards = []

        players_cards = []

        # House Cards
        while len(house_cards) != 2:
            house_cards.append(hit())
            if len(house_cards) == 2:
                print("Dealer has X &", house_cards[1])

        # Players Cards
        while len(players_cards) != 2:
            players_cards.append(hit())
            if len(players_cards) == 2:
                print("You have ", players_cards)

        #complete players hands
        while sum(players_cards) < 21:
            action_taken = str(input("Do you want to stay or hit?"))
            if action_taken == "hit":
                players_cards.append(hit())

         while sum(house_cards) < 17:
             house_cards.append(hit())

        #get result
        res = result(player_hand, house_hand)

        #output result
        elif "bust" == res or "lose" == res:
            dealers_score += 1
        elif "blackjack" == res or "win" == res:
            dealers_score += 1
        else: "push" == res 
            dealers_score += 1

        # Sum of the House Cards
        if sum(house_cards) == 21:
            dealer_score += 1
            print("The House has 21 and wins!")
        elif sum(house_cards) > 21:
            players_score += 1
            print("Dealer has busted!")

        # Sum of the Players Cards
        while sum(players_cards) < 21:
            action_taken = str(input("Do you want to stay or hit?"))
            if action_taken == "hit":
                players_cards.append(hit())
                print("You now have a total of " + str(sum(players_cards)) + " from these cards ", players_cards)
            else: 
                print("The dealer has a total of " + str(sum(house_cards)) + " with ", house_cards)
                print("You have a total of " + str(sum(players_cards)) + " with ", players_cards)
                if sum(house_cards) > sum(players_cards):
                    house_score += 1
                    print("You lose, The House wins!")
                else:
                    players_score += 1
                    print("You win! You beat the House!")
                    break

        if sum(house_cards) > 21:
            house_score += 1
            print("You BUSTED! The House wins this one.")
        elif sum(players_cards) == 21:
            players_score += 1
            print("You have BLACKJACK, you WIN! 21 baby!")

        print("Current Best of 3 Hands: ")
        print("Dealer: " + str(dealers_score) + " hands" + " - to - You: " + str(players_score) + " hands." )
        print("-------------------- Best---------------- OF--------------------3---------------------")
        total_hands += 1

play_game()
