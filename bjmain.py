
import multiprocessing
from BJTable import BJTable
from BJPlayer import BJPlayer
import pandas as pd
import pickle as pkl
from typing import List, Tuple
from multiprocessing import Pool, current_process
import numpy as np


def setup_table() -> Tuple[BJTable, BJPlayer]:
    t = BJTable()
    p1 = BJPlayer(1000)
    t.seat_player(p1)
    return t, p1


def play_game(t: BJTable, p1: BJPlayer):
    # strat = np.random.choice(list(p1.strategies.keys()))
    strat = p1.strategies["Hit on 16"]
    p1.bet = 10
    t.take_bets(p1, p1.bet)
    t.deal()
    p1.strategy = strat
    p1.play_hand(t, t.dealer.hand[0].value)
    t.dealer.play_hand(t)
    winnings = t.pay_out(p1)
    result_entry = {
        "player_id": p1.player_id,
        "player_name": p1.player_name,
        "dealer_up_card": t.dealer.get_up_card(),
        "dealer_up_card_value": t.dealer.get_up_card_value(),
        "dealer_final_hand_value": t.dealer.get_hand_value(),
        "dealer_busted": t.dealer.is_busted(),
        "dealer_blackjack": t.dealer.is_blackjack(),
        "dealer_final_hand": t.dealer.hand,
        "player_bet": p1.bet,
        "player_hand": p1.hand,
        "player_hand_value": p1.get_hand_value(),
        "player_busted": p1.is_busted(),
        "player_blackjack": p1.is_blackjack(),
        "player_won": t.is_winner(p1),
        "player_winnings": winnings,
        "player_stack": p1.stack,
        "player_strategy": strat
    }
    return result_entry


def run_process(i: int):
    print("Starting process {}".format(i))
    t, p1 = setup_table()
    results = pd.DataFrame(
        columns=[
            "player_id",
            "player_name",
            "dealer_up_card",
            "dealer_up_card_value",
            "dealer_final_hand_value",
            "dealer_busted",
            "dealer_blackjack",
            "dealer_final_hand",
            "player_bet",
            "player_hand",
            "player_hand_value",
            "player_busted",
            "player_blackjack",
            "player_won",
            "player_winnings",
            "player_stack",
            "player_strategy"
        ]
    )
    for j in range(1_000):
        if p1.stack <= p1.bet:
            break
        result_entry = play_game(t, p1)
        t.reset()
        results = results.append(result_entry, ignore_index=True)
    print("Finished process {} having played {} hands".format(i, j))
    return results


def main():

    pool = Pool(processes=5)
    results = pool.map(run_process, range(5))
    results = pd.concat(results)

    # results = run_process(0)

    # t, p1 = setup_table()
    # for _ in range(1_000):
    # result_entry = play_game(t, p1)
    # results = results.append(result_entry, ignore_index=True)
    # t.reset()

    results.to_pickle("results_1000.pkl")


if __name__ == "__main__":
    main()
