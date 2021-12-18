
from BJTable import BJTable
from BJPlayer import BJPlayer
import pandas as pd
import pickle as pkl
from typing import List, Tuple


def setup_table() -> Tuple[BJTable, BJPlayer]:
    t = BJTable()
    p1 = BJPlayer()
    t.seat_player(p1)
    return t, p1


def play_game(t: BJTable, p1: BJPlayer):

    t.deal()
    p1.play_hand(t)
    t.dealer.play_hand(t)
    result_entry = {
        "dealer_up_card": t.dealer.get_up_card(),
        "dealer_up_card_value": t.dealer.get_up_card_value(),
        "dealer_final_hand_value": t.dealer.get_hand_value(),
        "dealer_busted": t.dealer.is_busted(),
        "dealer_blackjack": t.dealer.is_blackjack(),
        "dealer_final_hand": t.dealer.hand,
        "player_hand": p1.hand,
        "player_hand_value": p1.get_hand_value(),
        "player_busted": p1.is_busted(),
        "player_blackjack": p1.is_blackjack(),
        "player_won": t.is_winner(p1),
        "player_stack": p1.stack
    }
    t.reset()
    return result_entry


def main():

    results = pd.DataFrame(
        columns=[
            "dealer_up_card",
            "dealer_up_card_value",
            "dealer_final_hand_value",
            "dealer_busted",
            "dealer_blackjack",
            "dealer_final_hand",
            "player_hand",
            "player_hand_value",
            "player_busted",
            "player_blackjack",
            "player_won",
            "player_stack"
        ]
    )

    t, p1 = setup_table()
    for _ in range(1_000):
        result_entry = play_game(t, p1)
        results = results.append(result_entry, ignore_index=True)
        t.reset()

    results.to_pickle("results_1000.pkl")


if __name__ == "__main__":
    main()
