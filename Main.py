print("Hey guyz!!")
print("Cosmo's Capable Coders for the W")


# This is where the main game functions will run.

# here we are importing random and the other two files player and deck and welcoming players

import random
from cards import deck
from player import player

print("Welcome to Two-Deck War!")

#Creating one deck per player and shuffling them
deck1 = deck()
deck2 = deck()

deck1.shuffle()
deck2.shuffle()

#Assigning players to their deck

player1 = player("Player 1", deck1)
player2 = player("Player 2", deck2)


#Keep the game going while both players still have cards
while not player1.deck.is_empty() and not player2.deck.is_empty():
    
    #Create a list and add all cards played in a round to the list. At the end the winner takes all the cards
    pile = []
    
    card1 = player1.deck.draw()
    card2 = player2.deck.draw()
    pile.extend([card1, card2])
    
    print(f"{player1.name} drew the {str(card1)}.")
    print(f"{player2.name} drew the {str(card2)}.")
    # While loop that makes a War when player one and two play cards with equal values
    # if a player runs out of cards the loop stops
    while card1.get_value() == card2.get_value() and not player1.deck.is_empty() and not player2.deck.is_empty():
        print("War!")
        
        card1 = player1.deck.draw()
        card2 = player2.deck.draw()
        pile.extend([card1, card2])
        
        print(f"{player1.name} drew the {str(card1)}.")
        print(f"{player2.name} drew the {str(card2)}.")
    
    #Shuffle the pile so the decks aren't in the same order every time
    random.shuffle(pile)
    
    # Function that allows the Higher card to win the pile
    if card1.get_value() > card2.get_value():
        player1.deck.add_cards(pile)
        print(f"{player1.name} wins the round!")
    elif card2.get_value() > card1.get_value():
        player2.deck.add_cards(pile)
        print(f"{player2.name} wins the round!")
    elif player1.deck.is_empty():
        #If a player runs out mid war the player with cards left takes the pile
        player2.deck.add_cards(pile)
    else:
        player1.deck.add_cards(pile)
    
    print(f"{player1.name} has {str(player1.deck.size())} cards.")
    print(f"{player2.name} has {str(player2.deck.size())} cards.")
    
    input("Press Enter to play the next round.")
    
#The player with cards left at the end wins the game
if player1.deck.is_empty():
    winner = player2
else:
    winner = player1
    
print(f"{winner.name} has collected all of the cards.")
print(f"{winner.name} wins the game!")
    