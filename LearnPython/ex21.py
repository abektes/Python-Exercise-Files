__author__ = 'ahmetbektes'

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions"


age = add (30, 5)
height = substract(72,10)
weight = multiply(10,10)
iq = divide (100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway:

print "Here is the puzzle."

what = add (age, substract (height, multiply(weight, divide(iq,2))))

print "That becomes:", what , "Can you do it by hand?"

