__author__ = 'ahmetbektes'

def gold_room():
	print '''
	This room is full of gold.
	How much do you want to take?'''

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Man,learn how to type a number!")

	if how_much < 50:
		print "Nice, you are not greeady, you are the winner!"
		exit(0)
	else:
		dead("You are gready bastard!")



def left_room():
	print "You see a big teddy bear in this room."
	print "Do you want to stay here with him or just walk away from coridor."
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "stay":
			dead("He just seems lovely but then slaps your face off!")
		elif next == "walk away" and not bear_moved:
			print "The bear is moved towards other direction.You can reach a door"
			print "Do you want to open the door?"
		elif next == "open door":
			gold_room()
		else:
			print "I don't understand it"



def right_room():

	print "Here you see the great devil."
	print ''' Do you flee or wait'''

	next = raw_input("> ")

	if "flee" in next:
		start()

	elif "wait" in next:
		dead("Well that was a tasty head!")
	else:
		right_room()


def dead(why):
	print why, "Good job!"
	exit(0)


def start():
	print "You are in a dark room."
	print "There is two door on your left and right"
	print "Please select one room!"

	next = raw_input("> ")

	if next == "left":
		left_room()
	elif next == "right":
		right_room()
	else:
		dead("You stumble around the room until you starve.")



start ()
