from Card import Card, suits, ranks
from random import shuffle, randrange
from typing import Iterator, List


class Deck(object):
    def __init__(self, n_decks: int = 1) -> None:
        self.cards: List[Card] = []
        self.n_decks: int = n_decks
        self.stack: float = 0.0
        self.shuffle()

    def shuffle(self) -> None:
        self.cards = []
        for _ in range(self.n_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))
        shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

    def __str__(self) -> str:
        return "Deck: " + str(self.cards)

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, key: int) -> Card:
        return self.cards[key]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value

    def __delitem__(self, key: int) -> None:
        del self.cards[key]

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)
