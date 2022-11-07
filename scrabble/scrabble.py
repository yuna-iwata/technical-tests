# started 11:40 -> 13:10
# plan 
# functions: 
# points() -> calc point for a letter
# pointsforword() -> calc points for word using points()
# drawseven() -> shuffle and draw seven tiles at random from bag
# findvalidword() -> using the tiles from drawseven() find a word from dictionary.txt
# longestvalidword() -> find the longest valid word  from findvalidword()
# plan the rest if i get that far

import random

def points(letter):
    letter_up = letter.upper()
    if(letter_up in ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']):
        return 1
    elif(letter_up in['D', 'G']):
        return 2
    elif(letter_up in['B', 'C', 'M', 'P']):
        return 3
    elif(letter_up in ['F', 'H', 'V', 'W', 'Y']):
        return 4
    elif(letter_up in ['K']):
        return 5
    elif(letter_up in ['J','X']):
        return 8
    elif(letter_up in ['Q','Z']):
        return 10

def points_for_word(word):
    total_points = 0
    split_word = list(word)
    for letter in split_word:
        total_points += points(letter)
    return total_points

def shuffle_drawseven():
    bag = 12*['E']+9*['A','I']+8*['O']+6*['N','R','T']+4*['L','S','U','D']+3*['G']+2*['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y']+1*['K', 'J', 'X', 'Q', 'Z']
    random.shuffle(bag)
    return bag

# tests
print(points('e')) #should be 1
print(points_for_word('guardian')) #should be 10
print(shuffle_drawseven())


# f = open('scrabble/dictionary.txt','r')
# words = []


# print(f)


