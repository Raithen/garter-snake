import random
class Deck:
    def __init__(self):
        self.cards = []

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)

    def _deal(self, num_cards=1):
        self.num_cards = num_cards
        if self.count() > 0:
            for num in range(num_cards):
                return self.cards.pop()
        return "All cards have been delt."

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            print("Only full decks can be shuffled!")

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num_cards):
        hand = []
        for num in range(num_cards):
            hand.append(self._deal())
        return hand


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

deck = Deck()
print(deck)
print(deck.cards)
deck.shuffle()
print(deck.cards)
card = deck.deal_card()
print(card)
hand = deck.deal_hand(5)
print(hand)
print(deck)
deck.shuffle()