from ITable import ITable
from Deck import Deck
from BJDealer import BJDealer
from Player import Player
from BJPlayer import BJPlayer


class BJTable(ITable):
    """
    BJTable Blackjack table

    Creates a Black Jack table that
      Receives bets from players
      Deals players two face up cards and the dealer one face up card and one face down card.
      Allows players to hit, stand, double or split.
      Dealer hits until hard 17 or greater.
      Players bust on over 21.
      Determines the winner and pay them
    """

    def __init__(self, n_decks=6) -> None:
        super().__init__(n_decks=n_decks)
        self.current_player = 0
        self.dealer: BJDealer = BJDealer()

    def deal(self):
        """
        deal 

        Deals two face up cards to each player and one face up and one face down to
        the dealer.
        """
        # for seat in range(len(self.players)):
        for player in self.players:
            for _ in range(2):
                player.hand.append(self.deck.deal())
        for _ in range(2):
            self.dealer.hand.append(self.deck.deal())

    def player_hit(self, player: BJPlayer):
        """
        player_hit 

        player hits and receives a card.
        """
        if not player.is_busted():
            player.hand.append(self.deck.deal())
        else:
            print(f"{player} is busted")

    def is_winner(self, player: BJPlayer) -> float:
        """
        is_winner 

        Returns 1 if player has won, 0 if the dealer has won and 0.5 if a push.
        """
        if player.is_busted():
            return 0
        elif self.dealer.is_busted():
            return 1
        elif player.is_blackjack() and not self.dealer.is_blackjack():
            return 1
        elif player.get_hand_value == self.dealer.get_hand_value():
            return 0.5
        else:
            return 1 if player.get_hand_value() > self.dealer.get_hand_value() else 0

    def reset(self):
        """
        reset 

        Resets the table for the next hand.
        """
        self.dealer.reset()
        for player in self.players:
            player.reset()
        self.deck.shuffle()
