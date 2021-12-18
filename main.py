from Game import Game
from Table import Table


def main():
    t = Table()
    g = Game(t)
    g.populate_table()
    g.play()
    g.table.players[0].place_bet(5)
    g.table.players[1].place_bet(15)
    g.table.players[2].place_bet(20)
    g.table.players[3].place_bet(25)
    g.table.players[4].place_bet(30)
    g.table.players[5].place_bet(35)
    t.deal_to_table()
    t.deal_to_table()
    t.deal_to_table()
    t.deal_to_table()
    t.deal_to_table()
    g.table.print_table()


if __name__ == "__main__":
    main()
