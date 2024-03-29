import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']

lives_remaining = 14

#why he did not use a list for keeping all the guess?
guessed_letters = ''

def play():
	word = pick_a_word()
	while True:
		guess = get_guess(word)
		if process_guess(guess, word):
			print "You win!"
			break
		if lives_remaining == 0:
			print ("You lost!")
			print ("The word was" + word)
			break

# Selecting a word from list randomly

def pick_a_word():
	word_position = random.randint(0, len(words) - 1)
	return words[word_position]


# Guessing structure

def get_guess(word):
	print_word_with_blanks(word)
	print ('Lives Remaining' + str(lives_remaining))
	guess = input ('Guess a letter?')
	return guess

def print_word_with_blanks(word):
	display_word = ''
	for letter in word:
		if guessed_letters.find(letter) > -1:
			display_word = display_word + letter
		else:
			display_word = display_word + '-'
	print(display_word)

def process_guess(guess, word):
	if len(guess) > 1:
		return whole_word_guess(guess,word)
	else:
		return single_letter_guess(guess, word)

def whole_guess(guess,word) :
	global lives_remaining
	if guess == word:
		return True
	else:
		lives_remaining = lives_remaining - 1
		return False

def single_letter_guess(guess,word) :
	global guessed_letters
	global lives_remaining

	if word.find(guess) == -1:
		lives_remaining = lives_remaining -1

	guessed_letters = guessed_letters + guess

	if all_letters_guessed(word):
		return True
	return False

def all_letters_guessed(word):
	for letter in word:
		if guessed_letters.find(letter) == -1:
			return False
		return True


print ('Lives Remaining' + str(lives_remaining))

play()

