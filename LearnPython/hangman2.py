__author__ = 'ahmetbektes'

## PyHangman (ver. 1.0) - CLI-based Hangman game written in Python
## © 2014 Alden Davidson <davidsonalden@gmail.com>
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License


import sys, random, os

class Gallows:
    def __init__(self):
        '''Visual of the game.'''
        self.state = [
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t        | ',
                '\t        | ',
                '\t        | ',
                '\t        | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t        | ',
                '\t        | ',
                '\t        | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t  |     | ',
                '\t  |     | ',
                '\t        | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t \|     | ',
                '\t  |     | ',
                '\t        | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t \|/    | ',
                '\t  |     | ',
                '\t        | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t \|/    | ',
                '\t  |     | ',
                '\t /      | ',
                '\t________|_',
            ],
            [
                '\t  _______ ',
                '\t  |     | ',
                '\t  O     | ',
                '\t \|/    | ',
                '\t  |     | ',
                '\t / \\    | ',
                '\t________|_',
            ]
        ]

    def set_state(self, misses):
        '''Sets the current visual being used.'''
        newState = ''

        state = self.state[misses] # set state to the list of desired gallows image
        # construct gallows image into str from list
        for piece in state:
            newState += piece + '\n'
        return newState


class ChooseWord:
    def __init__(self):
        '''Set the length of the wordlist.'''
        self.numLines = sum(1 for line in open('wordlist.txt'))

    def newWord(self):
        '''Choose a new word to be guessed.'''
        stopNum = random.randint(0, self.numLines-1) # establish random number to be picked from list
        # extract word from file
        with open("wordlist.txt") as file:
            for x, line in enumerate(file):
                if x == stopNum:
                    word = line.strip() # remove endline characters
        return word


class Letters:
    def blanks(self, word, blanks):
        '''Create blanks for each letter in the word.'''
        for letter in word:
            # Don't hide hyphens
            if letter == '-':
                blanks += '-'
            else:
                blanks += '_'
        return blanks

    def check_letter(self, word, guess, blanks, used, missed):
        '''Check if guessed letter is in the word.'''
        newWord = word
        # If the user presses enter without entering a letter
        if guess == '':
            raw_input("You have to guess something, silly!")
        # replace the corresponding blank for each instance of guess in the word
        elif guess in word and guess not in used:
            for x in range(0, word.count(guess)):
                blanks[newWord.find(guess)] = guess
                newWord = newWord.replace(guess, '-', 1) # replace already checked letters with dashes
            used += guess # add the guess to the used letter list
        # If the user inputs a letter they've already used
        elif guess in used:
            raw_input("You already tried that letter, silly!")
        # If the user inputs multiple letters at once
        elif len(list(guess)) > 1:
            raw_input("You can't guess more than one letter at a time, silly!")
        #If the guess is wrong
        else:
            missed = True
            used += guess
        return blanks, used, missed


class Engine:
    def __init__(self):
        '''Initialize all variables for the game'''
        self.wrongGuesses = 0 # number of incorrect guesses
        self.currentImg = "" # current state of the gallows
        self.word = "" # word to be guessed
        self.blanks = [] # blanks which hide each letter of the word until guessed
        self.used =[] # list of used letters

    def setup(self, image, getWord, letters, finish):
        self.__init__()
        self.currentImg = image.set_state(self.wrongGuesses)
        self.word = getWord.newWord()
        self.blanks = letters.blanks(self.word, self.blanks)
        self.play(image, getWord, letters, finish)

    def play(self, image, getWord, letters, finish):
        missed = False

        newPage()
        print self.currentImg
        for x in self.blanks:
            print x,
        print '\n'
        for x in self.used:
            print x,
        print '\n'

        guess = raw_input("Guess a letter: ")
        blanks, self.used, missed = letters.check_letter(self.word, guess, self.blanks, self.used, missed)

        if missed == True and self.wrongGuesses < 6:
            self.wrongGuesses += 1
            self.currentImg = image.set_state(self.wrongGuesses)
            self.play(image, getWord, letters, finish)
        elif missed == False and blanks != list(self.word) and self.wrongGuesses != 6:
            self.play(image, getWord, letters, finish)
        elif blanks == list(self.word):
            finish.victory(self, image, getWord, letters)
        else:
            finish.game_over(self, image, getWord, letters)



class EndGame:
    def game_over(self, game, image, getWord, letters):
        newPage()
        print "Nice try! Your word was '%s'." % game.word
        while True:
            play_again = raw_input("Play again? [y/n]")
            if 'y' in play_again:
                game.setup(image, getWord, letters, self)
            elif 'n' in play_again:
                sys.exit(0)
            else:
                print "Huh?"

    def victory(self, game, image, getWord, letters):
        newPage()
        print "Congratulations, you win!"
        print "You correctly guessed the word '%s'!" % game.word
        while True:
            play_again = raw_input("Play again? [y/n]")
            if 'y' in play_again:
                game.setup(image, getWord, letters, self)
            elif 'n' in play_again:
                sys.exit(0)
            else:
                print "Huh?"



def newPage():
    '''Clears the window.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    image = Gallows()
    getWord = ChooseWord()
    letters = Letters()
    finish = EndGame()
    game = Engine()

    newPage()
    print("\nWelcome to Hangman!")
    print("Guess the word before the man is hung and you win!")
    raw_input("\n\t---Enter to Continue---\n")
    newPage()

    game.setup(image, getWord, letters, finish)



if __name__ == '__main__':
    main()