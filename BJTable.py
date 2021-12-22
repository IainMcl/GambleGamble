from ITable import ITable
from Deck import Deck
from BJDealer import BJDealer
from Player import Player
from BJPlayer import BJPlayer
from typing import Optional, List


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

    def get_player_options(self, player: BJPlayer) -> List[str]:
        if player.is_blackjack() or player.is_busted() or player.get_hand_value() == 21:
            options = ["Stand"]
        elif self.dealer.hand[0].value == 1:
            options = ["Hit", "Stand", "Double", "Insurance"]
        elif len(player.hand) == 2:
            options = ["Hit", "Stand", "Double", "Surrender"]
            if player.hand[0].value == player.hand[1].value:
                options.append("Split")
        else:
            options = ["Hit", "Stand"]
        return options

    def play_hand(self, player: BJPlayer, option: str) -> None:
        """
        play_hand

        Plays a hand of Blackjack for the player.
        returns False if the player is busted or has chosen to stand.
        returns True if the player has chosen to hit.
        """
        if option == "Hit":
            self.player_hit(player)
            return True
        elif option == "Stand":
            return False
        elif option == "Double":
            self.take_bets(player, player.bet * 2)
            self.player_hit(player)
            return False
        elif option == "Insurance":
            if self.dealer.hand[0].value == 1:
                player.insurance = True
                self.take_bets(player, player.bet / 2)
            return True
        elif option == "Surrender":
            player.surrendered = True
            return False
        elif option == "Split":
            return False
        else:
            raise Exception(f"{option} is not a valid option.")

    def take_bets(self, player: BJPlayer, bet: float) -> None:
        """
        take_bets

        Takes the player's bet and checks to make sure it is valid.
        """
        if bet <= 0:
            raise Exception("Bet must be greater than 0.")
        elif bet > player.stack:
            raise Exception(
                "Bet must be less than or equal to the player's stack.")
        else:
            player.bet = bet
            player.stack -= bet

    def pay_out(self, player: BJPlayer) -> float:
        """
        pay_out

        Pays the player their bet and resets the player for the next hand.
        """
        if player.surrendered:
            win = player.bet / 2
            player.stack += win
            return win
        elif player.insurance and self.dealer.is_blackjack():
            # insurance pays 2 to 1
            player.stack += player.bet
            return player.bet
        elif self.is_winner(player) == 1:
            win = player.bet * 2
            player.stack += win
            return win
        elif self.is_winner(player) == 0.5:
            player.stack += player.bet
            return player.bet
        elif self.is_winner(player) == 0:
            return 0
        else:
            raise("Iain you messed up with pay out options.")
