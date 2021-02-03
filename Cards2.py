import random
from tkinter import *
#from tkinter import ttk


"""This is code to allow people to play cards virtually, remotely, over the internet.  Playing Cards 
implements a deck of cards, dealing cards face up or face down, discarding cards, multiple players. """

class Deck:
    """This class handle cards and the deck"""
    def __init__(self):
        """These are the cards Hearts, Clubs, Spades, Diamonds, Ace, King, Queen, Jake, 1-10  """

        self.cards = [  # 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'AK',
            # 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']
        self.top_card = self.cards[0]


    def print_all_cards(self, cards):
        self.cards = cards
        for self.card in self.cards:
            print(self.card)

    def shuffle(self):
        """This code shuffles the cards."""
        for x in range(1150):
            self.pos = random.randint(1, len(self.cards) + 1)
            self.temp = self.cards[0]
            self.cards.remove(self.cards[0])
            self.cards.insert(self.pos, self.temp)
            self.pos = random.randint(1, len(self.cards) + 1)
            self.temp = self.cards[-1]
            self.cards.remove(self.cards[-1])
            self.cards.insert(-self.pos, self.temp)

    def cut(self):
        """This code cuts the cards after a user input"""
        # num = int(input('To cut the deck, select a number between 1 and ' + str(len(cards)) + '? '))
        self.temp_cards = self.cards[:8]
        for self.temp_card in self.temp_cards:
            self.cards.remove(self.temp_card)
            self.cards.append(self.temp_card)

    def get_top_card(self):
        return self.cards[0]

    def get_second_card(self):
        return self.cards[1]

    def remove_top_card(self):
        self.cards.remove(cards[0])

    def pop_top_card(self):
        self.cards.pop(0)

    def deck_on_table(self):
        self.root = table.get_root()
        self.deck_button = Button(self.root, width=self.deck_width, height=self.deck_height, text=self.top_card)
        self.deck_button.pack(padx=self.deck_xposition, pady=self.deck_yposition)
        self.root.mainloop()

    def deal_cards(self, number_of_cards, face):
        """This function deals a specific number of cards all players from the deck """
        self.number_of_cards = number_of_cards
        self.face = face
        # self.number_of_cards = number_of_cards
        for x in range(0, self.number_of_cards):
            for player in self.players:
                self.player.add_card_to_hand(self.cards.pop(0), self.face)

    def pop_and_get_top_card(self):
        self.hold_card = self.get_top_card()
        self.pop_top_card()
        return self.get_top_card()




class Player:
    """ Class Player class contains player name (variable), hand of cards - face up or down (2 dimension list),
    and pot (variable) """

    def __init__(self, name):
        self.player_hand = []
        self.player_discard = []
        self.player_name = name
        self.pot = 0
        self.player_hand = [["a1", False], ["a2", False], ["a3", False]]
        # self.player_hand = ["??", False]

    def get_player_hand(self):
        """ Gets the list of cards with face up/down for a player"""
        return self.player_hand

    def get_player_name(self):
        """ Gets the players name """
        return self.player_name

    def set_player_name(self, name):
        """ Sets the players name """
        self.player_name = name

    def get_player_pot(self):
        """Gets the player's pot """
        return self.pot

    def set_player_pot(self, amount):
        self.pot = amount

    def add_card_to_hand(self, card_name, isVisible):
        self.card = [card_name, isVisible]
        self.player_hand.append(self.card)


    def get_player_cards(self):
        """Get the cards in the players hand. """
        return map(lambda i: i[0], self.player_hand)

    def get_card_face(self):
        """ Get if the card is face up or down """
        # print(self.player_hand)
        return self.player_hand[0][1]

    def get_card_in_hand(self, discard_card):
        """ finds card in hand to move to discard list
        """
        self.discard_card = discard_card
        for card in player_discard:
            if card == self.discard_card:
                return card
        else:
            print(self.discard_card + 'Not found')

players = []
"""  players is a list of players.  (players are a class) """


def print_all_players(players):
    for player in players:
        print(player.player_name, player.player_hand, player.pot, player.player_discard)


def add_player(player, name):
    """ add_player adds a player (class) to a list of all players."""
    player_name = name
    player = player
    temp = Player()
    temp.player_name = player_name
    players.append(temp)

def get_player_via_name(players, name_of_player):
    for player in players:
        if name_of_player == player.player_name:
            return player


def player_discard_card(self, name_of_player):
    for player in players:
        if player.player_name == name_of_player:
            temp_card = player.player_hand[0]
            player.player_discard.append(temp_card)
            player.player_hand.remove(temp_card)



class Table:
    """This class is the playing table which hands the gui """

    def __init__(self):
        self.deck = deck
        self.root = Tk()
        self.root.geometry("1350x700")

        #image = Image.open("C:\gui\Keith.jpg")
        #image = image.resize((100, 300))
        #image = ImageTk.PhotoImage(image)

        self.deck_width = 20
        self.deck_height = 10
        self.deck_xposition = 20
        self.deck_yposition = 220

        self.top_card = deck.get_top_card()

        self.deck_button = Button(self.root, width=self.deck_width, height=self.deck_height, text=self.top_card, command=self.new_top_card)
        self.deck_button.pack(padx=self.deck_xposition, pady=self.deck_yposition)


        self.root.mainloop()


    def new_top_card(self):
        self.top_card = self.deck.pop_and_get_top_card()
        self.deck_button.config(text="New Top Card  " + self.top_card)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    deck.cut()
    print("   before dealing ")
    print(deck.cards)


    table = Table()
    print("  After dealing    ")
    print(deck.cards)




    player1 = Player('Keith')
    players.append(player1)
    player2 = Player('Annabelle')
    players.append(player2)
    player3 = Player('Steve')
    players.append(player3)
    player1.set_player_pot(100)
    player2.set_player_pot(200)
    player3.set_player_pot(300)

    #deal_cards(2, False)
    #deal_cards(1, True)

    #print("   Players hands ")
    #print_all_players(players)

    #print('     deck of cards after dealing ')
    #print(cards)

    print('     player hands after discards  ')
    print_all_players(players)


    #player_discard_card(players, 'Steve')
    #print_all_players(players)





