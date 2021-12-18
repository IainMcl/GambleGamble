from Card import Card
from Deck import Deck
from typing import List, Optional
import itertools
from IPlayer import IPlayer


class Player(IPlayer):

    def __init__(self, stack: Optional[float] = None) -> None:
        # initialise parent IPlayer class
        super().__init__()
        self.stack: float = stack
        self.bet: float = 0.0

    def place_bet(self, amount: float) -> None:
        self.bet = amount
        self.stack -= amount
