
import random
#import letter_scores

#langauges movedto classes
class English(): #267,753 words
    language = 'en'
    filepath = 'sowpods.txt' 
    bag_of_letter_tiles = list('?'*2 + 'e'*12 + 'a'*9 + 'i'*9 + 'o'*8 + 'n'*6 + 'r'*6 + 't'*6 + 'l'*4 
                            + 's'*4 + 'u'*4 + 'd'*4 + 'g'*3 + 'b'*2 + 'c'*2 + 'm'*2 + 'p'*2 + 'f'*2 
                            + 'h'*2 + 'v'*2 + 'w'*2 + 'y'*2 + 'kjxqz')
    letter_points = {
        'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
        'd':2, 'g':2, 
        'b':3, 'c':3, 'm':3, 'p':3, 
        'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 
        'k':5, 
        'j':8, 'x':8,
        'q':10, 'z':10,
        '?':0
    }

class Polish(): #works but WARNING because of cases and genders, there are over 3 MILLION entries 
    language = 'pl'
    filepath = 'slowa.txt'
    bag_of_letter_tiles = list('?'*2 + 'a'*9 + 'i'*8 +'e'*7 + 'o'*6 + 'n'*5 + 'z'*5 + 'r'*4 + 's'*4 + 'w'*4  +'y'*4 
                    + 'c'*3 + 'd'*3 + 'k'*3 + 'l'*3 + 'm'*3 + 'p'*3 + 't'*3 + 'b'*2 + 'g'*2 + 'h'*2 
                    + 'j'*2 + 'ł'*2 + 'u'*2 + 'ąęfóśżćńź')
    letter_points = {
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


def create_lexicon():
    #Read from filepath and populate list
    with open (language.filepath, 'r', encoding = 'utf-8') as file:
            return [line.rstrip() for line in file] #rstrip to remove whitespace line by line


def fill_tilebag():
#populate the tilebag list with the predetermined amount of each tile
    return language.bag_of_letter_tiles


def valid_word_checker(tiles, wilds, word):
    if len(word) > len(tiles): #if the length is wrong, skip everything because obv that's impossible
        return -1
    
    wordscore = 0
    miss_counter = 0 
    temp_tiles = tiles.copy() #tiles[:] or tile.copy() or list(tiles) is necessary BECAUSE OTHERWISE = IS JUST IS REFERENCE TO THE FIRST LIST WTF WHY
    #print(f"tiles {temp_tiles}")
    for letter in word:
        if letter in temp_tiles:
            wordscore += language.letter_points[letter]
            temp_tiles.remove(letter)
            #print(f'tiles {temp_tiles} word {word} wordscore = {wordscore}')
        elif len(temp_tiles) == 0:
            break
        else:
            miss_counter += 1 
            #word_score += 0
            
    if miss_counter <= wilds:
        return wordscore
    else:
        return -1 #invalid word


def validate_and_score_words(tiles, lexicon):
    valid_words = {}
    wordscore = 0
    temp_tiles = tiles.copy()
    #count wilds, remove them from list, now they exist only as a concept
    wilds = temp_tiles.count('?')
    while temp_tiles.count('?') > 0: #loop because .remove only removes first instance of element
        temp_tiles.remove('?')

    #nested for loops checking each word of the dictionary, then each letter
    for word in lexicon:
        #print(f"word {word} tiles {tiles} temptiles {temp_tiles}")
        wordscore = valid_word_checker(temp_tiles, wilds, word)
        if wordscore > 0:
            valid_words[word] = wordscore

    return valid_words #dict of word:score


#ok, let's get started!
desired_language = input("English(en) or Polish(pl)?\n")
if desired_language == 'en' or desired_language.lower() == 'english':
    language = English()
elif desired_language == 'pl' or desired_language.lower() == 'polish' or desired_language.lower() == 'polski':
    language = Polish()
else:
    print('Invalid input')

print('Scrabble Practice! Try to get the highest scoring word from your available tiles!') #until the tiles run out? Can do but later

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
tilebag = tilebag[7:]
print(f'Your hand: {player1.hand}')
#print(tilebag)

typed_word = input("Type a word to score!\n")

validated_words = validate_and_score_words(player1.hand, lexicon)

if len(validated_words) == 0:
    print("Whoa, there are no valid words in this hand. That's not supposed to happen!")
elif typed_word in validated_words: 
    wordscore = validated_words[typed_word]
    print(f"Nice! You scored {wordscore} points!")
    
    #create list of all values (possible scores) from validated words, and use set() to remove duplicates
    possible_scores = list(set(validated_words.values())) 
    possible_scores.sort(reverse=True)

    #determine rank of typed_word, compared to other possible scores
    rank = possible_scores.index(wordscore) + 1
    if rank == possible_scores[0]:
        print("Wow! You nailed it! You hit the top rank of points with the maximum possible score!")
    else:
        print(f'Your word score rank was {rank}! (The top score at rank 1 was: {possible_scores[0]})')
else:
    print('Invalid word...')
    print('Here were all the possible words, sorted from highest to lowest score:')
    print(dict(sorted(validated_words.items(), key=lambda item: item[1], reverse=True)))


