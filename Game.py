from Table import Table
from Player import Player


class Game:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        self.table.deal()

    def populate_table(self):
        for i in range(self.table.seats):
            self.table.players.append(Player(100.0))

    def print_table(self):
        pass
