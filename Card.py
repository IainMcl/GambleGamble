from typing import List, Dict

suits: Dict[str, str] = {
    'S': 'Spades',
    'H': 'Hearts',
    'D': 'Diamonds',
    'C': 'Clubs'
}

ranks: Dict[str, int] = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()
        self.name = self.get_name()

    def get_value(self):
        if self.rank == 'A':
            return 1
        elif self.rank in ['T', 'J', 'Q', 'K']:
            return 10
        else:
            return int(self.rank)

    def get_name(self):
        return self.rank + self.suit

    def __str__(self):
        return self.name
