
#import deck class from cards to be used in player class
from cards import deck

#player class to store player name, and player deck
class player:

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    #Player plays the top card of their deck and returns it
    def play_card(self):
        card = self.deck.draw()
        return card

    #Player collects a list of won cards and adds them to the bottom of their deck
    def collect_cards(self, cards):
        self.deck.add_cards(cards)

    #Returns how many cards the player has
    def card_count(self):
        return self.deck.size()

    #Returns True if the player still has cards to play, False if they are out
    def has_cards(self):
        return not self.deck.is_empty()
