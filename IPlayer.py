
from Card import Card
from Deck import Deck
from typing import List
import itertools
from abc import ABC, abstractmethod


class IPlayer(ABC):
    newid = itertools.count()

    def __init__(self) -> None:
        self.player_id: int = next(IPlayer.newid)
        self.player_name: str = "Player {}".format(self.player_id)
        self.hand: List[Card] = []

    def __str__(self) -> str:
        return self.player_name

    def print_hand(self, new_line: bool = True) -> None:
        print(self.player_name, end=": ")
        for card in self.hand:
            print(card, end=' ')
        if new_line:
            print()

    def reset(self) -> None:
        self.hand = []
