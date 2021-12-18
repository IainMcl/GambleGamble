from Player import Player
from typing import Optional, List
from ITable import ITable


class BJPlayer(Player):

    def __init__(self, stack: Optional[float] = None) -> None:
        super().__init__(stack)

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

    def print_hand(self, new_line: bool = True) -> None:
        super().print_hand(False)
        print(f"({self.get_hand_value()})", end=" ")
        if self.is_busted():
            print("BUSTED", end="")
        if new_line:
            print()

    def play_hand(self, table: ITable) -> None:
        while not self.is_busted() and self.get_hand_value() <= 11:
            self.hand.append(table.deck.deal())
