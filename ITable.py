import itertools
from Deck import Deck
from Player import Player
from Card import Card
from typing import List
from abc import ABC, abstractmethod


class ITable(ABC):
    """
    ITable Interface for a card table class.
    """
    newid = itertools.count()

    def __init__(self, n_decks=1) -> None:
        self.table_id: int = next(ITable.newid)
        self.table_name: str = f"Table {self.table_id}"
        self.deck = Deck(n_decks=n_decks)
        self.seats: int = 6
        self.players: List[Player] = []
        self.current_player: int = 0

    @abstractmethod
    def deal(self) -> None:
        """
        Deal cards to players.
        """
        pass

    def seat_player(self, player: Player) -> None:
        if len(self.players) < self.seats:
            self.players.append(player)
        else:
            raise Exception("Table is full.")

    def remove_player(self, player: Player) -> None:
        self.players.remove(player)
