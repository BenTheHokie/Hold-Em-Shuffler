def flushable(board): #Detect if a flush can be made with the board
    suitcount={'C':0,'H':0,'S':0,'D':0}
    for c in board:
        suitcount[c[-1:].upper()]+=1
        if suitcount[c[-1:].upper()]==3:
            suit = c[-1:].upper() #If there are three of the same suit, the hand is "flushable"
    try:                          #we assume only one suit can be flushable
        return {'s':suit,'n':suitcount[suit]}
    except NameError:
        return False

def straight(hand,board):
    cards = hand+board
    nums=[]
    trans={'J':11,'Q':12,'K':13,11:'J',12:'Q',13:'K',1:'A',14:'A'} #the "translation" dictionary
    for c in cards:
        c=c[0:len(c)-1].upper()
        if c=='A' and not (1 in nums):
            nums+=[1,14] #ace can count as high or low in straights
        else:
            try:
                if not int(trans[c]) in nums: #Check if a face card and if it is, just add the number equivalent
                    nums+=[int(trans[c])]
            except KeyError:
                if not int(c) in nums: #if not, just add the number
                    nums+=[int(c)]
    nums.sort()
    nums.reverse()
    print nums
    for n in range(len(nums)-4):
        #print nums[n:n+5],range(nums[n],nums[n]-5,-1)
        if nums[n:n+5]==range(nums[n],nums[n]-5,-1): #Count down from the top to get the best possible straight
            return nums[n] #Return the top number
    return False 

def besthand(board, hands):
    board=['7H', 'JH', 'QC', '7C', '6C']
    f=flushable(board)
    if f:
        fhands=[]
        for h in range(len(hands)):
            if ([h][0][-1:]==hands[h][1][-1:]) and (hands[h][0][-1:].upper()==f['s']):
                fhands+=[h]
        if len(fhands)==1:
            return {'hnum':fhands[0],'hand':'Flush'}