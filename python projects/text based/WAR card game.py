from random import shuffle

class Card:
    
    def __init__(self, rank, suit):
        values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,'jack':11,'queen':12, 'king':13, 'ace':14}
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank.capitalize() + ' of ' + self.suit.capitalize()

class Deck:
    def __init__(self):
        suits = ('spades', 'clubs', 'diamonds', 'hearts')
        ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack', 'ace')
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Player:

    def __init__(self):
        self.hand = []

    def play(self):
        return self.hand.pop(0)
        pass

    def shuffle(self):
        shuffle(self.hand)    

    def add(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)


'''
new_deck = Deck()
new_deck.shuffle()
card = new_deck.deal()
print(len(new_deck.all_cards))
print(new_deck.all_cards[-1])
player = Player('Mishal')
player.add([card, card, card])
new = player.play()
print(player)
'''
player1 = Player()
player2 = Player()
table = Player()
deck = Deck()
deck.shuffle()
#print(len(deck.all_cards))
while deck.all_cards:
    player1.add(deck.deal())
    player2.add(deck.deal())
    #print(len(deck.all_cards))

while True: 

    input('Press enter to play a card\n')

    opp_card = player2.play()
    user_card = player1.play()
    table.add([opp_card, user_card])
    table.shuffle()

    print(f"Your card: {user_card}")
    print(f"Opponent's card: {opp_card}\n")

    if user_card.value > opp_card.value:
        print('You won the round')
        player1.add(table.hand)
        table = Player()
            

    elif user_card.value < opp_card.value:
        print(f'Opponent won the round')
        player2.add(table.hand)
        table = Player()
            
    else:
        print('WAR!!')
    
        if len(player1.hand) <= 3 and len(player1.hand) == len(player2.hand):
            print('Both players are unable to play WAR\nTIE GAME')
            break
        
        elif len(player1.hand) < len(player2.hand) and len(player1.hand) < 3:
            print('You are unable to play WAR\nYOU LOST THE GAME')
            break
            
        elif len(player2.hand) < len(player1.hand) and len(player2.hand) < 3:
            print('Opponent is unable to play WAR\nYOU WON THE GAME!!')
            break
        else:
            for i in range(0,5):
                table.add(player1.play())
                table.add(player2.play())
                
    if len(player1.hand) == 0:
        print('You have no cards left\nYOU LOST THE GAME')
        break
    elif len(player2.hand) == 0:
        print('Opponent has no cards left\nYOU WON THE GAME')
        break
    else:    
        print(f'You have {len(player1.hand)} cards left\n')
    
