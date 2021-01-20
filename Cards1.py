import random

"""This is code to allow people to play cards virtually, remotely, over the internet.  Playing Cards 
implements a deck of cards, dealing cards face up or face down, discarding cards, multiple players. """

cards = [  # 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'AK',
    # 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
    # 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']



def print_all_cards(cards):
    for card in cards:
        print(card)



class Player:
    """ Class Player class contains player name (variable), hand of cards - face up or down (2 dimension list),
    and pot (variable) """


    def __init__(self):
        self.player_hand = []
        self.player_name = "name?"
        self.pot = 0
        self.player_hand = [["a1", False], ["a2", False], ["a3", False]]
        #self.player_hand = ["??", False]

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

    def get_player_card(self):
        """Get the cards in the players hand. Used in get_all_cards  """
        return self.player_hand[0][0]

    def get_card_face(self):
        """ Get if the card is face up or down """
        #print(self.player_hand)
        return self.player_hand[0][1]

    def get_all_cards(self):
        """Get all the cards in a players hand """
        x = 0        #self.player = player
        player_cards = []
        for card in self.player_hand:
            player_cards.append(self.player_hand[x][0])
            x = x + 1
        return player_cards

players = []
"""  players is a list of players.  (players are a class) """

def print_all_players(players):
    for player in players:
        print(player.player_name, player.player_hand, player.pot)



def add_player(player, name):
    """ add_player adds a player (class) to a list of all players."""
    player_name = name
    player = player
    temp = Player()
    temp.player_name = player_name
    #print(temp.player_name)
    players.append(temp)
    #print("  from add_player")

    #print(players[0])


def deal_cards(players, number_cards, face):
    pass


def shuffle():
    """This code shuffles the cards."""
    for x in range(1150):
        pos = random.randint(1, len(cards) + 1)
        temp = cards[0]
        cards.remove(cards[0])
        cards.insert(pos, temp)
        pos = random.randint(1, len(cards) + 1)
        temp = cards[-1]
        cards.remove(cards[-1])
        cards.insert(-pos, temp)



def cut():
    """This code cuts the cards after a user input"""
    # num = int(input('To cut the deck, select a number between 1 and ' + str(len(cards)) + '? '))
    temp_cards = cards[:8]
    for temp_card in temp_cards:
        cards.remove(temp_card)
        cards.append(temp_card)


if __name__ == '__main__':
    shuffle()
    cut()
    print(cards)


    player1 = Player()
    players.append(player1)
    player2 = Player()
    players.append(player2)
    player3 = Player()
    players.append(player3)
    print_all_players(players)
    print(player1.get_all_cards())
    #print(player1.get_player_card())




#  Disregard below, this is for testing
    # print(player1.player_name)
    # player1.set_player_name('Mary K')
    # print(player1.get_player_name())
    # player2.set_player_name("Sally F")
    # print(player2.get_player_name())
    # print(player3.get_player_name())

    # print(players[0].player_name)
    # print(players[1].player_name)
    # print(players[2].player_name)

    #print(players)
    #players.append(add_player(Player, "Harry"))
    #playerx0 = players[0]
    #print(playerx0)

    # print(player1.player_hand[0][0])
    # print(player1.get_player_hand())
    # print(player1.get_player_name())
    # print(player1.get_player_pot())
    # print(player1.get_player_card())
    # print(player1.get_card_face())
    # print('        Get all Cards     ')
    # print(player1.get_all_cards())

