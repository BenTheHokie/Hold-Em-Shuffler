import random
import os
cls = lambda: os.system('cls')
rand=random.randint

def asciicard(card):
    suits={'h':'''.------.
|A_  _ |
|( \/ )|
| \  / |
|  \/ A|
`------\''''.split('\n'),'d':'''.------.
|A /\  |
| /  \ |
| \  / |
|  \/ A|
`------\''''.split('\n'),'c':'''.------.
|  _   |
| ( )  |
|(_x_) |
|  Y   |
`------\''''.split('\n'),'s':'''.------.
|A .   |
| / \  |
|(_,_) |
|  I  A|
`------\''''.split('\n')}
    
    retcard=suits[card[-1:].lower()] #get the suit as ascii art retcard is the card that will eventually be returned
    if card[:2]=='10':    #if there's a 10 there's two characters we have to change
        lnrepl=list(retcard[1]) #lnrepl is the line that is being modified
        lnrepl[1:3]=['1','0']
        retcard[1]=''.join(lnrepl)
        lnrepl=list(retcard[4])
        lnrepl[5:7]=['1','0']
        retcard[4]=''.join(lnrepl)
        return retcard
    else:
        lnrepl=list(retcard[1]) #split the first second line of the ascii art into a list
        lnrepl[1:2]=card[0] #change the character to the correct one
        retcard[1]=''.join(lnrepl) #regenerate the list back into a string
        lnrepl=list(retcard[4]) #do the same with the opposite corner
        lnrepl[6:7]=card[0]
        retcard[4]=''.join(lnrepl)
        return retcard

def shuff():
    nums=['A']+range(2,11)+['J','Q','K'] #make an ordered deck
    suits=list('CDHS')
    ordeck=[]
    deck=[]
    for s in suits:
        for n in nums:
            ordeck+=[str(n)+s]
    for i in range(len(ordeck)):
        deck+=[ordeck.pop(rand(0,len(ordeck)-1))] #pick a random card out of the ordered deck
    return deck

def prtlns(*args):
    final=''
    for l in range(len(args[0])): #for each line, concatenate the first line of the 1st, 2nd, 3rd.... list
        for a in args:            #i.e. concatenate the top edges of the cards, then the middles etc.
            final+=a[l]
        final+='\n'
    return final

while True:
    deck=shuff()
    #hand=[deck.pop(0),deck.pop(0)] #pop pulls the card out of the deck so it can't be used again
    #hand2=[deck.pop(0),deck.pop(0)]
    #hand3=[deck.pop(0),deck.pop(0)]
    #hand4=[deck.pop(0),deck.pop(0)]    
    hands = []
    for i in range(4):
        hands+=[[deck.pop(0),deck.pop(0)]]
    board=[deck.pop(0),deck.pop(0),deck.pop(0)]
    
    for h in hands:
        print prtlns(asciicard(h[0]),asciicard(h[1]))
    raw_input()
    cls()
    for h in hands:
        print prtlns(asciicard(h[0]),asciicard(h[1]))
    print prtlns(asciicard(board[0]),asciicard(board[1]),asciicard(board[2]))
    board+=[deck.pop(0)]
    raw_input()
    cls()
    
    for h in hands:
        print prtlns(asciicard(h[0]),asciicard(h[1]))
    print prtlns(asciicard(board[0]),asciicard(board[1]),asciicard(board[2]),asciicard(board[3]))
    board+=[deck.pop(0)]    
    raw_input()
    cls()
    
    for h in hands:
        print prtlns(asciicard(h[0]),asciicard(h[1]))
    print prtlns(asciicard(board[0]),asciicard(board[1]),asciicard(board[2]),asciicard(board[3]),asciicard(board[4]))
    raw_input()
    cls()