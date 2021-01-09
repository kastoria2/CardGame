import numpy as np
import random


class Cards:
    def __init__(self):
        self.deck_state = []
        self.deck_size = 5
        self.to_card_position = 0
        self.from_card_position = 0
        self.to_card_name = '  '
        self.from_card_name = ' '
        self.ordr = 0
        self.item = 0
        self.card_value = ''
        self.element = " "
        self.cut_number = 0

        np.deck_state = [
            ["A1", "A2", "A3", "A4", "A5"],  # Card name
            [1, 2, 3, 4, 5],  # Card Position in deck
            ["deck", "deck", "deck", "deck", "deck"],  # Card Pile (deck, hand, table
            [0, 0, 0, 0, 0],  # player holding card
            [False, False, False, False, False]  # Card visible
        ]

    def prt_deck_state(self):
        for item in np.deck_state:
            print(item)

    def get_card(self, item, ordr):
        self.item = 0
        self.ordr = ordr
        self.card_value = np.deck_state[item][ordr]
        return self.card_value

    def swap_element(self, element, swap1_position, swap2_position):
        self.temp = element
        self.element = 0
        self.swap1_position = swap1_position
        self.swap2_position = swap2_position
        self.value1 = self.get_card(0, self.swap1_position)
        self.value2 = self.get_card(0, self.swap2_position)
        np.deck_state[0][self.swap1_position] = self.value2
        np.deck_state[0][self.swap2_position] = self.value1

    def shuffle_deck(self):
        for x in range(0, 50):
            self.position1 = random.randint(0, self.deck_size-1)
            self.position2 = random.randint(0, self.deck_size-1)
            self.swap_element("name", self.position1, self.position2)

    def cut_deck(self, cut_number):
        self.cut_number = cut_number



deck = Cards()
print(" done with creating deck")
deck.prt_deck_state()
print(' ')
deck.shuffle_deck()
deck.prt_deck_state()