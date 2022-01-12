import random

def clr():
    print('\n'*100)
class Card():
    VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, '10':10, 'K':10, 'Q':10, 'J':10, 'A':11}
    def __init__(self, name):
        pass


class Deck(list):
    def __init__(self):
        self.restock()
        #super().__init__()

    def shuffle(self):
        random.shuffle(self)


    def take_card(self):
        return self.pop()

    def is_empty(self):
        return len(self) == 0

    def restock(self):
        for name in Card.VALUES:
            self.append(name)
            self.append(name)
            self.append(name)
            self.append(name)

class Hand(list):

    def __init__(self, owner='dealer'):
        self.owner = owner
        self.hand = f'             {self.owner.upper()}   ||'
        super().__init__()

    def hit(self, deck):
        self.append(deck.pop())
        if self.owner == 'dealer' and len(self)==2:
            self.hidden = self[-1]
            self.hand += '     *     ||'
        else:
            self.hand += f'     {self[-1]}     ||'

    def eval(self):
        handsum = 0
        elevens = self.count('A')
        for card in self:
            handsum += Card.VALUES[card]
        #take 1 instead of 11 for aces
        if self.owner!='dealer':
            while handsum > 21 and elevens != 0:
                elevens -= 1
                handsum -= 10
        return handsum

    def unhide(self):
        self.hand = self.hand.replace('*', self.hidden)
        update()

def win(kind, name='player'):
    dealer.unhide()
    if kind == 'standoff':
        print('STANDOFF')
    else:
        print(f'{kind.upper()}\n{name.upper()} WINS')
    exit()

def update():
    print(dealer.hand)
    print(player.hand)



    
deck = Deck()
deck.shuffle()

player = Hand('player')
dealer = Hand()

player.hit(deck)
dealer.hit(deck)
player.hit(deck)
dealer.hit(deck)





update()

if player.eval()==dealer.eval()==21:
     clr()
     win('standoff')
elif player.eval()==21:
    clr()
    win('blackjack', 'player')
elif dealer.eval()==21:
    clr()
    win('blackjack', 'dealer')



while True:
    inp = input()
    clr()
    if inp == 'hit':
        player.hit(deck)
    if player.eval()==21:
        clr()
        win('blackjack', 'player')
    if player.eval()>21:
        clr()
        win('bust', 'dealer')
    if inp == 'stand':
        break
    update()


while dealer.eval()<=17:
    dealer.hit(deck)
    print('DEALER HITS')
    if dealer.eval()==21:
        win('blackjack', 'dealer')
    if dealer.eval()>21:
        win('bust', 'player')
    update()
print('DEALER STANDS')


if player.eval()>dealer.eval():
    dealer.unhide() 
    print('PLAYER WINS')
elif player.eval()<dealer.eval():
    dealer.unhide() 
    print('DEALER WINS')
else:
    dealer.unhide()    
    print('STANDOFF')

