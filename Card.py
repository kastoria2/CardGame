import random


def prt_cards(Card):
    """This method prints all the attributes of the cards in the deck.  This is used for testing"""
    cards = Card
    x = 0
    for item in cards:
        print(cards[x].card_name)
        x += 1


class Card:
    """ Card is an object that holds all the attributes of a card.
        Card name, positon of card in deck, the pile the cards is in 'deck, hand, discard
        the player who is holding the card in their hand
        the card is visible - face up or not visiable - face down"""

    # card_name = ' '  # name of the card [H}earts, [S}pades. [D]iamonds, [C]lubs

    def __init__(self, name, num):
        self.card_name = name


card_names = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'AK',
              'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
              'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
              'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']


def make_deck():
    """ This fucntion makes a deck of cards."""
    x = 0
    for item in card_names:
        # cards.append(item)
        cards.append(Card(card_names[x], x))
        x += 1


def shuffle_deck():
    """This function shuffles the deck  """
    for x in range(0, 100):
        position1 = random.randint(0, len(cards) - 1)
        position2 = random.randint(0, len(cards) - 1)
        cards[position2].card_position = position1
        cards[position1].card_position = position2
        sort_deck_by_position()  # this sort is needed to maintain non-duplicate deck positions.


def sort_deck_by_position():
    """This sorts the deck of cards by the deck order (card_position)"""
    # cards.sort(key=lambda card: card.card_position)
    pass


def cut_deck(self, num):
    self.cut_postion = num


if __name__ == '__main__':
    print(card_names)





    print("creating deck of cards")
    #cards = []
   # make_deck()
    # shuffle_deck()
    #prt_cards(cards)
