from BJPlayer import BJPlayer
from Card import Card
from typing import List
from ITable import ITable


class BJDealer(BJPlayer):
    def __init__(self):
        super().__init__()
        self.player_name = "Dealer"

    def play_hand(self, table: ITable) -> None:
        """
        Dealer plays hand.
        """
        while not self.is_busted() and self.get_hand_value() < 17:
            self.hand.append(table.deck.deal())

    def get_up_card(self) -> Card:
        """
        Return the dealer's up card.
        """
        return self.hand[0]

    def get_up_card_value(self) -> int:
        """
        Return the dealer's up card value.
        """
        return self.hand[0].value
