__author__ = 'ahmetbektes'

i = 0

numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

# What is the difference between a for and while loop?

print '''

for - can only operate over a collection of things.
while - any kind of iteration you want and harder to get it right.'''