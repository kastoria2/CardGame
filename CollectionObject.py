import self as self


cardhand = [['a1', True], ['b1', False]]
cardhand.append(['c1', False])
cardhand.append(['c1', False])
cardhand_temp = cardhand[2]
print(cardhand[2])
cardhand.remove(cardhand_temp)

hand = cardhand[2]
print(hand[0])
print(hand[1])










class Player:
    self.player_name = ' Jim '
    self.hand = ['??']
    pot = 0

    def __init__(self):
        self.player_name = "Steve"
        self.hand = ">>"
        self.pot = 0

    def get_player_name(self):
        return self.player_name

    def get_hand(self):
        return self.hand

    def get_pot(self):
        return self.pot


class Collection_Players:
    def __init__(self):
        self.players = []

    def add_player(self):
        self.players.append(Player)

    def get_player(self):
        return self


if __name__ == '__main__':
    #player1 = Player
    #print(player1)
    #print(player1.get_player_name(player1()))
    #print(player1.get_hand(player1()))
    #print(player1.get_pot(player1()))

    print(cardhand)
