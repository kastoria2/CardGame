import random
"""This refactored code treats cards in a list.  This code also shuffles a deck and cuts a deck.  
This code is quite simple.  Much simpler than the previous code.  I have commented out the Hearts, Spades, 
and club cards, just so have less printout to read and review."""


cards = [#'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'AK',
              #'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
              #'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
              'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']


def shuffle():
    """This code shuffles the cards."""
    for x in range(1150):
        pos = random.randint(1, len(cards)+1)
        temp = cards[0]
        cards.remove(cards[0])
        cards.insert(pos, temp)

def cut():
    """This code cuts the cards after a user input"""
    temp_cards = []
    num = int(input('To cut the deck, select a number between 1 and 13?'))
    for x in range(0, num):
        temp = cards[0]
        cards.remove(cards[0])
        cards.append(temp)


if __name__ == '__main__':
    print("               the deck of cards before shuffling.")
    print(cards)
    print("                The deck of cards after shuffling")
    shuffle()
    print(cards)
    cut()
    print("                  The deck of cards after cutting")
    print(cards)
