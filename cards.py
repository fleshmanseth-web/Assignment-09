import random

#Here we are creating a class for cards
#We have crated a dictionary that holds the cards value with its respective rank
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

#The card class should contain: value, suit, rank
class card:
    #We initialize the card
    def __init__(self, rank, suit):
        self.rank = rank
        self.value = card_values[rank]
        self.suit = suit
#Here we are creating a class for decks
#Initialization: constructor that creates a list of 52 card objects and shuffle them
#Methods
    #Draw a card and move cards up
    #Add cards to the bottom of the deck

#Things they said they needed
class deck:

    #In the initialization function, a list is created with each of
    #the 52 cards in the deck and then shuffled.
    def __init__(self):
        self.cards_in_deck = []
        for suit in suits:
            for rank in ranks:
                new_card = card(rank, suit)
                self.cards_in_deck.append(new_card)
        #This is the part that shuffles the deck
        random.shuffle(self.cards_in_deck)

    def return_deck(self):
        current_rank = self.cards_in_deck[3].rank
        return current_rank

    #Draw() function
    def draw(self):
        first_card = self.cards_in_deck.pop(0)
        return first_card

    #Add_card(cards)
    def add_cards(self, cards):
        self.cards_in_deck.extend(cards)

    #Check to see how many cards are in the deck
    def size(self):
        return len(self.cards_in_deck)

    #Checks to see if the deck is empty
    def is_empty(self):
        empty = False
        if len(self.cards_in_deck) == 0:
            empty = True
        return empty