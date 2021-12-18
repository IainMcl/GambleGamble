from typing import List
from Player import Player
from Deck import Deck
from Card import Card
from ITable import ITable


class Table(ITable):

    def __init__(self) -> None:
        # initialise parent ITable class
        super().__init__(n_decks=1)
        self.community_cards: List[Card] = [Card('-', '0') for _ in range(5)]
        self.pot: float = 0.0
        self.current_bet: float = 0.0
        self.current_round: int = 0
        self.current_bet_player: int = 0
        self.current_bet_amount: float = 0.0
        self.current_bet_type: str = 'none'
        self.sb = 0.5
        self.bb = 1.0

    def deal(self, n_cards: int = 2) -> None:
        for seat in range(self.seats):
            for _ in range(n_cards):
                self.players[seat].hand.append(self.deck.deal())
        self.current_round = 1
        self.current_bet_type = 'ante'
        self.current_bet_amount = 0.0
        self.current_bet_player = 0
        self.current_bet = 0.0
        self.pot = 0.0
        self.current_player = 0

    def deal_to_table(self) -> None:
        self.community_cards[self.current_round - 1] = self.deck.deal()
        self.current_round += 1

    def __str__(self) -> str:
        return "Table: " + str(self.table_id) + " '" + self.table_name + "' " + "seats: #" + str(self.seats)

    def get_pot(self) -> float:
        self.pot += sum([player.bet for player in self.players])
        return self.pot

    def print_table(self) -> None:
        print("Table: " + str(self.table_id) + " '" +
              self.table_name + "' " + "seats: #" + str(self.seats))

        print(f"Pot: {self.pot}              {self.table_name}                ")
        print(f"--------------------------------------------------------------")
        print(
            f"               {self.players[2].player_name}                    {self.players[3].player_name}            ")
        print(
            f"                {self.players[2].stack}                       {self.players[3].stack}           ")
        print(
            f"                {self.players[2].hand[0]} {self.players[2].hand[1]}                       {self.players[3].hand[0]} {self.players[3].hand[1]}           ")
        print(f"             ----------------------------------------           ")
        print(
            f"            /    {self.players[2].bet}                         {self.players[3].bet}     \          ")
        print(f"           /                                          \         ")
        print(
            f"{self.players[1].player_name}  |                   Pot: {self.get_pot()}                 |  {self.players[4].player_name}")
        print(
            f" {self.players[1].stack}    |  {self.players[1].bet}           {self.community_cards[0]} {self.community_cards[1]} {self.community_cards[2]} {self.community_cards[3]} {self.community_cards[4]}         {self.players[4].bet}  |   {self.players[4].stack}")
        print(
            f" {self.players[1].hand[0]} {self.players[1].hand[1]}    |                                            |   {self.players[4].hand[0]} {self.players[4].hand[1]}")
        print(f"          |                                            |        ")
        print(f"           \                                          /         ")
        print(
            f"            \    {self.players[0].bet}                         {self.players[5].bet}     /           ")
        print(f"             ----------------------------------------           ")
        print(
            f"                {self.players[0].hand[0]} {self.players[0].hand[1]}                       {self.players[0].hand[0]} {self.players[0].hand[1]}           ")
        print(
            f"               {self.players[0].player_name}                    {self.players[5].player_name}            ")
        print(
            f"                {self.players[0].stack}                       {self.players[5].stack}           ")
