__author__ = 'ahmetbektes'

the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','appricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

for number in the_count:
	print "This is a count %d" % number

# same as above

for fruit in fruits:
	print "a fruit type: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

for i in range (0,6):
	print "Adding %d to the list." %i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i

