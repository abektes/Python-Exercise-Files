from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I am the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """

Ok, so you said %r about liking me. You are living %r and you have a %r computer.

""" % (likes, lives, computer)