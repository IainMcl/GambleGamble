from Card import Card
from Deck import Deck
from typing import List


class Player(object):
    def __init__(self) -> None:
        self.hand: List[Card] = []
        self.stack: float = 0.0
