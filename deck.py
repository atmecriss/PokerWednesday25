import random

class Card:
    Ranks = ["2", "3","4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    Suits = ["♣", "♦", "♥", "♠"]
    def __init__(self, suit, rank):
        if rank not in self.Ranks:
            raise ValueError("Invalid rank")
        if suit not in self.Suits:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.Ranks.index(self.rank) > self.Ranks.index(other.rank)

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()
    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
         return self._rank


class Deck:
        def __init__(self):
            self._deck = []
            for suit in Card.Suits:
                for rank in Card.Ranks:
                    self._deck.append(Card(suit, rank))

        def __str__(self):
            return str(self._deck)

        def shuffle(self):
            random.shuffle(self._deck)

        def deal(self):
            return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
