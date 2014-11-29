print "You enter a dark room with two doors. Do you go through door 1 or door 2?"

door = raw_input(">tell me now")

if door == "1":
	print "There is a giant bear here eating a cheese cake. What do you do?"
	print "1 Take the cream"
	print "2 Scream at the bear"

	bear = raw_input(">")

	if bear == 1:
		print "The bear eats your face off, good job!"
	elif bear == 2:
		print "The bear eats your legs off, good job!"

	else:
		print "Well, doing %s is better. Bear runs away" % bear

if door == "2":
	print "Stay there"
	print "1 turn on the light"
	print "2 take a deep breath and take your step"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "The door is closed behind you!"
	else:
		print "Screaming is starting right now!"

else:
	print "You stumble around and fall on a knife and die. Good Job"

