__author__ = 'ahmetbektes'

print "Mary had a little lamb."
print "Its fleece was white as %s" % 'snow'

print "." * 10 #What'd that do?


end1 = "C"
end2 = "heese"
end4 = "B"
end5 = "urger"


print end1 + end2,
print end4 + end5


formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said tonight."
)


# Exercise 9.py

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:" , days
print "Here are the months:", months
print """

There is something going on here.
With the three double-quoutes.
We ll be able to much as We like
Wven 4 or maybe 6 or more.

"""

# Exercise 10.py

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = " I'm \\a \\ cat."

fat_cat = """

I ll do a list:

\t* Cat food
\t* Fishes
\t* Catnip \n\t* Grass

"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

