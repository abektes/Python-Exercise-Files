__author__ = 'ahmetbektes'

import datetime

class Person(object):
	def __init__(self):
		'''
		create a person called name
		'''
		self.name = name
		self.birthday = None
		self.lastName = name.split(' ')[-1]

	def getLastName(self):

		return self.lastName

	def setBirthday(self,month,day,year):
		'''
		:param month: month of the birthday
		:param day: day of the birthday
		:param year: year of the date
		:return: gives the full date
		'''

		if self.birthday == None:
			raise ValueError

		return (datetime.date.today() - self.birthday).days

	def __lt__(self, other):
		'''
		:param other:
		:return: True if self's name is lexicographically less
		than the other's name. and False otherwise...
		'''

		if self.lastName == other.lastName:
			return self.lastName < other.lastName

		return self.lastName < other.lastName

	def __str__(self):
		return self.name




class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print self.incantation


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())


class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print "A.x"
    def y(self):
        print "A.y"
    def z(self):
        print "A.z"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print "B.y"
    def z(self):
        print "B.z"

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print "C.y"
    def z(self):
        print "C.z"

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print "D.z"


obj = D()
print obj.a
print obj.b
print obj.c
print obj.d

obj.x()
obj.y()
obj.z()