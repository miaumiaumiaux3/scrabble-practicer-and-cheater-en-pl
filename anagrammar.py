
import random
#import letter_scores

#dict of all letter points (don't think there's a way to combine it and probs not worth)
letter_points_en = {
    'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
    'd':2, 'g':2, 
    'b':3, 'c':3, 'm':3, 'p':3, 
    'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 
    'k':5, 
    'j':8, 'x':8,
    'q':10, 'z':10,
    '*':0
}

letter_points_pl = {
    'a':1, 'i':1, 'e':1, 'o':1, 'n':1, 'z':1, 'r':1, 's':1, 'w':1,
    'y':2, 'c':2, 'd':2, 'k':2, 'l':2, 'm':2, 'p':2, 't':2,
    'b':3, 'g':3, 'h':3, 'j':3, 'ł':3, 'u':3,
    'ą':5, 'ę':5, 'f':5, 'ó':5, 'ś':5, 'ż':5,
    'ć':6,
    'ń':7,
    'ź':9,
    '*':0
}

class player:
    name = 'player'
    hand = []

def fill_tilebag(lang = 'en'):
#populate the tilebag list with the predetermined amount of each tile
    if lang == 'en':
        return list('*'*2 + 'e'*12 + 'a'*9 + 'i'*9 + 'o'*8 + 'n'*6 + 'r'*6 + 't'*6 + 'l'*4 + 's'*4 + 'u'*4 
                  + 'd'*4 + 'g'*3 + 'b'*2 + 'c'*2 + 'm'*2 + 'p'*2 + 'f'*2 + 'h'*2 + 'v'*2 + 'w'*2 + 'y'*2
                  + 'kjxqz')
    elif lang == 'pl':
        return list('*'*2 + 'a'*9 + 'i'*8 +'e'*7 + 'o'*6 + 'n'*5 + 'z'*5 + 'r'*4 + 's'*4 + 'w'*4  +'y'*4 
                    + 'c'*3 + 'd'*3 + 'k'*3 + 'l'*3 + 'm'*3 + 'p'*3 + 't'*3 + 'b'*2 + 'g'*2 + 'h'*2 
                    + 'j'*2 + 'ł'*2 + 'u'*2 + 'ąęfóśżćńź')
    else:
        print('Invalid lang string')

#def grab

#create instance of tilebag
tilebag = fill_tilebag() 
random.shuffle(tilebag) #shake tilebag
print(tilebag)

'''this is the part where it branches, it can either slowly deplete the bag to 'finish' the game, 
or it can just randomize and grab the first 7.... tbh both are easy, so let's have it deplete like a 'real' game'''

#give 7 tiles to player's hand and pop those tiles out of tilebag