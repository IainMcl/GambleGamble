# Gamble Gamble

A selection of analysis of different card games.

## Black Jack

A Black Jack simulator aiming to derive basic strategy from probabilistic events
observed over many games.

A Player `BJPlayer` at a `BJTable` where they make decisions to play Black Jack
aiming to beat the `BJDealer`.

The player can choose from a veriaty of different strategies. These will be
chosen at random initially where strategies include things like `Hit on 16` etc.
With time this will develop on to include more refined rules, likely determined
via decision tree based on observed information within the game. This
information includes:

- The players hold cards
- The dealers up card
- The running count (using high-low)
- The true count (running count / number of decks remaining)
- The players bet / stack sizes
- The relative risk to the player
