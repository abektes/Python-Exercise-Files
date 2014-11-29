__author__ = 'ahmetbektes'

import math

def sq(x):
	return x * x

class Coordinate(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "<"+str(self.x)+", "+str(self.y)+">"

	def distance(self,second):
		return math.sqrt(sq(self.x -second.x)+ sq(self.y-second.y))

c = Coordinate (3,4)
Origin = Coordinate(0,0)

print c.distance(Origin)


class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)

print w1.getx()