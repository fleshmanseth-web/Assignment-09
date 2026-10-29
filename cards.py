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