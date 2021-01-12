def prt_cards():
    """This method prints all the attributes of the cards in the deck.  This is used for testing"""
    for x in range(0, len(cards)):
        print(cards[x].card_name, cards[x].card_position, cards[x].pile, cards[x].player_holdg_card,
              cards[x].card_visible)


class Card:
    """ Card is an object that holds all the attributes of a card.
        Card name, positon of card in deck, the pile the cards is in 'deck, hand, discard
        the player who is holding the card in their hand
        the card is visible - face up or not visiable - face down"""
    card_name = ' '  # name of the card [H}earts, [S}pades. [D]iamonds, [C]lubs
    card_position = 0  # Casignates which pile the card is in - deck, hand, table, discard
    player_holdg_card = 0  # the player holding the card
    card_visible = False  # True indiecates card is faceup, False indicates the card is face down

    def __init__(self, name, num):
        self.card_name = name
        self.card_position = num
        self.pile = 'deck'
        self.player_holdg_card = 0
        self.card_visible = False


card_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'AJ', 'AQ', 'AK',
              'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
              'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
              'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']

def make_deck():
    """ This fucntion makes a deck of cards."""
    x = 0
    for item in range(0, len(card_names)):
        cards.append(Card(card_names[x], x))
        x += 1


print("creating deck of cards")
cards = []
make_deck()
print("printing cards")
prt_cards()


# S1 = Card("S1", 1)
# cards.append(S1)
# S2 = Card("S2", 2)
# cards.append(S2)
# cards.append(Card("S3", 3))

# cards[0].card_visible = True
# cards[0].pile = "table"
# cards[0].player_holdg_card = 1

