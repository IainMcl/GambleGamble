class HandRankings(object):
    """
    """

    def __init__(self):
        """
        """
        self.hand_rankings = {
            'High Card': 1,
            'Pair': 2,
            'Two Pair': 3,
            'Three of a Kind': 4,
            'Straight': 5,
            'Flush': 6,
            'Full House': 7,
            'Four of a Kind': 8,
            'Straight Flush': 9
        }

    def get_hand_ranking(self, hand):
        """
        """
        if self.is_straight_flush(hand):
            return self.hand_rankings['Straight Flush']
        elif self.is_four_of_a_kind(hand):
            return self.hand_rankings['Four of a Kind']
        elif self.is_full_house(hand):
            return self.hand_rankings['Full House']
        elif self.is_flush(hand):
            return self.hand_rankings['Flush']
        elif self.is_straight(hand):
            return self.hand_rankings['Straight']
        elif self.is_three_of_a_kind(hand):
            return self.hand_rankings['Three of a Kind']
        elif self.is_two_pair(hand):
            return self.hand_rankings['Two Pair']
        elif self.is_pair(hand):
            return self.hand_rankings['Pair']
        else:
            return self.hand_rankings['High Card']

    def is_straight_flush(self, hand):
        """
        """
        if self.is_flush(hand) and self.is_straight(hand):
            return True
        else:
            return False

    def is_four_of_a_kind(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values.count(values[0]) == 4:
                return True
        return False

    def is_full_house(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values.count(values[0]) == 3 and values.count(values[1]) == 2:
                return True
        return False

    def is_flush(self, hand):
        """
        """
        if len(hand) == 5:
            suits = [card.suit for card in hand]
            if suits.count(suits[0]) == 5:
                return True
        return False

    def is_straight(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values[0] == 'Ace':
                values.append('King')
            if values[0] == 'King':
                values.append('Queen')
            if values[0] == 'Queen':
                values.append('Jack')
            if values[0] == 'Jack':
                values.append('Ten')
            if values[0] == 'Ten':
                values.append('Nine')
            if values[0] == 'Nine':
                values.append('Eight')
            if values[0] == 'Eight':
                values.append('Seven')
            if values.count(values[0]) == 5:
                return True
        return False

    def is_three_of_a_kind(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values.count(values[0]) == 3:
                return True
        return False

    def is_two_pair(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values.count(values[0]) == 2 and values.count(values[1]) == 2:
                return True
        return False

    def is_pair(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values.count(values[0]) == 2:
                return True
        return False

    def is_royal_flush(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values[0] == 'Ace' and values[1] == 'King' and values[2] == 'Queen' and values[3] == 'Jack' and values[4] == 'Ten':
                return True
        return False

    def is_high_card(self, hand):
        """
        """
        if len(hand) == 5:
            values = [card.value for card in hand]
            if values[0] == 'Ace' or values[0] == 'King' or values[0] == 'Queen' or values[0] == 'Jack' or values[0] == 'Ten':
                return True
        return False
