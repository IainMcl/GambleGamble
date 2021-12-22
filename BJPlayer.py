from Player import Player
from typing import Optional, List
from ITable import ITable
import numpy as np


class BJPlayer(Player):
    insurance = False
    surrendered = False
    doubled = False
    strategies = {
        "Hit on 11": "h11",
        "Hit on 12": "h12",
        "Hit on 13": "h13",
        "Hit on 14": "h14",
        "Hit on 15": "h15",
        "Hit on 16": "h16",
        "Hit on 17": "h17",
        "Hit on 18": "h18",
        "Hit on 19": "h19",
        "Hit on 20": "h20",
        "Hit on 21": "h21",
        "Random": "random"
    }

    def __init__(self, stack: Optional[float] = None) -> None:
        super().__init__(stack)
        self.strategy = self.strategies["Hit on 16"]

    def choose_strategy(self, dealer_up_card: int) -> None:
        pass

    def place_bet(self, amount: float) -> None:
        self.bet = amount
        self.stack -= amount

    def is_busted(self) -> bool:
        return self.get_hand_value() > 21

    def is_blackjack(self) -> bool:
        return (self.hand[0].value == 1 and self.hand[1].value == 10) or (self.hand[0].value == 10 and self.hand[1].value == 1)

    def get_hand_value(self) -> int:
        value = sum(card.value for card in self.hand)
        if self.has_ace():
            value += 10
            if value > 21:
                value -= 10
        return value

    def has_ace(self) -> bool:
        return any(card.value == 1 for card in self.hand)

    def reset(self) -> None:
        self.hand = []
        self.bet = 0.0
        self.insurance = False
        self.surrendered = False
        self.doubled = False

    def print_hand(self, new_line: bool = True) -> None:
        super().print_hand(False)
        print(f"({self.get_hand_value()})", end=" ")
        if self.is_busted():
            print("BUSTED", end="")
        if new_line:
            print()

    def play_hand(self, table: ITable, dealer_up_card: int) -> None:
        if self.is_busted():
            return
        if self.strategy == "h11":
            while self.get_hand_value() <= 11:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h12":
            while self.get_hand_value() <= 12:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h13":
            while self.get_hand_value() <= 13:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h14":
            while self.get_hand_value() <= 14:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h15":
            while self.get_hand_value() <= 15:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h16":
            while self.get_hand_value() <= 16:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h17":
            while self.get_hand_value() <= 17:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h18":
            while self.get_hand_value() <= 18:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h19":
            while self.get_hand_value() <= 19:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h20":
            while self.get_hand_value() <= 20:
                self.hand.append(table.deck.deal())
        elif self.strategy == "h21":
            while self.get_hand_value() <= 21:
                self.hand.append(table.deck.deal())
        elif self.strategy == "random":
            while (options := table.get_player_options(self)) != ["Stand"]:
                table.play_hand(self, choice := np.random.choice(options))
                if choice == "Stand":
                    break
        else:
            raise ValueError(f"Invalid strategy: {self.strategy}")
