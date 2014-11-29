__author__ = 'ahmetbektes'


class lister(object):
	""" this is a list of integers that is going to be stored in the instance
	"""

	def __init__(self):
		self.list = []

	def insert(self, e):

		if not e in self.list:
			self.list.append(e)

	def member(self, e):
		return e in self.list

	def remove(self,e):

		try:
			self.list.remove(e)
		except:
			raise ValueError (str(e) + 'not found')

	def __str__(self):

		return '{' + ','.join([str(e) for e in self.list]) + '}'

	def intersect(self,other):

		commonValueSet = lister()

		#Go through the values in this set
		for list in self.list:
			if other.member(list):
				commonValueSet.insert(list)
		return commonValueSet

		self.list self.other

		except:
			raise ValueError

	def __len__(self):
		return len(self.list)


s = lister()

s.insert(3)
s.insert(5)

print s

s.remove(3)

print s
s.member(5)


### First Class :)

class Queue(object):

    def __init__(self):
        "Initializes 1 attribute: a list to keep track of the queue's elements"
        self.qlist = []

    def insert(self, element):
        "Adds an element to the attribute list using append"
        self.qlist.append(element)

    def remove(self):
        "Removes an element from the attribute list"
        # Check if the list is empty; if so then raise a ValueError
        if self.qlist == []:
            raise ValueError()
        else:
            # Otherwise we want to remove the first element from the list
            # and return that to the user.
            element = self.qlist[0]
            self.qlist.remove(element)
            return element
            # Could also do this in 1 line:
            # return self.qlist.pop(0)


class Queue(object):
    """ This is the object that needs a list which is going to be stored."""
    def _init(self):
        self.lista = []

    def insert(self,e):
        self.lista.append(e)

    def remove(self):
        if self.lista == []:
            raise ValueError
        else:
            e = self.lista[0]
            self.lista.remove(e)
            return e

