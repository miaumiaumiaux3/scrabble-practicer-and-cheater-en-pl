
import random
#import letter_scores

#choose language, global var AF
language = 'en' #267,753 words
#language = 'pl' #works but WARNING because of cases and genders, there are over 3 MILLION entries 

#dict of all letter points (don't think there's a way to combine it and probs not worth)
letter_points_en = {
    'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
    'd':2, 'g':2, 
    'b':3, 'c':3, 'm':3, 'p':3, 
    'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 
    'k':5, 
    'j':8, 'x':8,
    'q':10, 'z':10,
    '?':0
}

letter_points_pl = {
    'a':1, 'i':1, 'e':1, 'o':1, 'n':1, 'z':1, 'r':1, 's':1, 'w':1,
    'y':2, 'c':2, 'd':2, 'k':2, 'l':2, 'm':2, 'p':2, 't':2,
    'b':3, 'g':3, 'h':3, 'j':3, 'ł':3, 'u':3,
    'ą':5, 'ę':5, 'f':5, 'ó':5, 'ś':5, 'ż':5,
    'ć':6,
    'ń':7,
    'ź':9,
    '?':0
}

class Player:
    def __init__(self, name ='Player'):
        self.name = name
        self.hand = []
        
    #     self._hand = []

    # @property
    # def hand(self):
    #     return self._hand

    # @hand.setter
    # def hand(self, newhand):
    #     self._hand = newhand


def create_lexicon():
    if language == 'en':
        #Read from sowpods.txt and populate list
        with open ('sowpods.txt', 'r') as file:
            return [line.rstrip() for line in file] #rstrip to remove whitespace line by line
    elif language == 'pl':
        with open ('slowa.txt', 'r') as file:
            return [line.rstrip() for line in file] 
    else:
        #invalid language, but should be impossible because global var
        pass


def fill_tilebag():
#populate the tilebag list with the predetermined amount of each tile
    if language == 'en':
        return list('?'*2 + 'e'*12 + 'a'*9 + 'i'*9 + 'o'*8 + 'n'*6 + 'r'*6 + 't'*6 + 'l'*4 + 's'*4 + 'u'*4 
                  + 'd'*4 + 'g'*3 + 'b'*2 + 'c'*2 + 'm'*2 + 'p'*2 + 'f'*2 + 'h'*2 + 'v'*2 + 'w'*2 + 'y'*2
                  + 'kjxqz')
    elif language == 'pl':
        return list('?'*2 + 'a'*9 + 'i'*8 +'e'*7 + 'o'*6 + 'n'*5 + 'z'*5 + 'r'*4 + 's'*4 + 'w'*4  +'y'*4 
                    + 'c'*3 + 'd'*3 + 'k'*3 + 'l'*3 + 'm'*3 + 'p'*3 + 't'*3 + 'b'*2 + 'g'*2 + 'h'*2 
                    + 'j'*2 + 'ł'*2 + 'u'*2 + 'ąęfóśżćńź')
    else:
        print('Invalid language string, though that should be impossible since its a global variable')


def valid_word_checker(tiles, wilds, word):
    wordscore = 0
    miss_counter = 0 
    temp_tiles = tiles.copy() #tiles[:] or tile.copy() or list(tiles) is necessary BECAUSE OTHERWISE = IS JUST IS REFERENCE TO THE FIRST LIST WTF WHY
    #print(f"tiles {temp_tiles}")
    for letter in word:
        if letter in temp_tiles:
            if language == 'en':
                wordscore += letter_points_en[letter]
            elif language == 'pl':
                wordscore += letter_points_pl[letter]
            temp_tiles.remove(letter)
            #print(f'tiles {temp_tiles} word {word} wordscore = {wordscore}')
        elif len(temp_tiles) == 0:
            break
        else:
            miss_counter += 1 
            #word_score += 0
            #invalid word, go to next word in list
    if miss_counter <= wilds:
        return wordscore
    else:
        return -1


def validate_and_score_words(tiles, lexicon):
    valid_words = {}
    wordscore = 0
    
    #count wilds, remove them from list, now they exist only as a concept
    wilds = tiles.count('?')
    while tiles.count('?') > 0: #loop because .remove only removes first instance of element
        tiles.remove('?')

    #nested for loops checking each word of the dictionary, then each letter
    for word in lexicon:
        #print(f"word {word} tiles {tiles} temptiles {temp_tiles}")
        wordscore = valid_word_checker(tiles, wilds, word)
        if wordscore > 0:
            valid_words[word] = wordscore

    return valid_words #dict of word:score



#read dictionary of valid words from file and put into list
lexicon = create_lexicon()

#create instance of tilebag
tilebag = fill_tilebag() 
random.shuffle(tilebag) #shake tilebag
#print(tilebag)

'''now we create a player to give tiles that will refill from the tilebag as they're used until tilebag is empty and no valid words remain in hand -- aka endgame'''

#create player
player1 = Player() #if more than one player, on creation of second player, set player1 name to Player1

#give 7 tiles to player's hand and pop those tiles out of tilebag
player1.hand = tilebag[0:7]
print(player1.hand)
tilebag = tilebag[7:]
#print(tilebag)

validated_words = validate_and_score_words(player1.hand, lexicon)

print(dict(sorted(validated_words.items(), key=lambda item: item[1], reverse=True)))


#current error
#['e', 'e', 'c', 'b', 'a', 'a', 'd']
#{'abecedarian': 12, 'abecedarians': 12, <- literally impossible, so why is it passing? do we need to do a length check?