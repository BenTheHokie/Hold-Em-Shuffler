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
    lnrepl=list(retcard[1]) #split the first second line of the ascii art into a list
    lnrepl[1:len(card)]=list(card[0:len(card)-1]) #change the character to the correct one keeping in mind, the number might be 10 in which case we have to make space for two letters (taken care of by using len(card)) lnrepl is the line that is being modified
    retcard[1]=''.join(lnrepl) #regenerate the list back into a string
    lnrepl=list(retcard[4])    #do the same with the opposite corner
    lnrepl[8-len(card):7]=list(card[0:len(card)-1])
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

def prtlns(args):
    final=''
    for l in range(len(args[0])): #for each line, concatenate the first line of the 1st, 2nd, 3rd.... list
        for a in args:            #i.e. concatenate the top edges of the cards, then the middles etc.
            final+=a[l]
        final+='\n'
    return final

def prthands():
    for h in hands:
        print prtlns([asciicard(h[0]),asciicard(h[1])])

def prtboard():
    bcards=[]
    for c in board:
        bcards+=[asciicard(c)]
    print prtlns(bcards)

while True:
    deck=shuff()
    hands = []
    for i in range(4):
        hands+=[[deck.pop(0),deck.pop(0)]]
    board=[deck.pop(0),deck.pop(0),deck.pop(0)]
    
    prthands()
    raw_input()
    cls()
    
    for i in range(3):
        prthands()
        prtboard()
        board+=[deck.pop(0)]
        a = raw_input()
        cls()
    if a=='x': break