print "Let's practice everything."
print 'You \'d need to know \'bout escapes with \\ that do \n newlines \t tabs.'

poem = '''

\t Seni seviyorum
Bu mantigi anladiginda sonrasinda
neler \nyapabilecegini bildiginde
ya da hissettiginde \n \t \t bir dusunsene.

'''

print "----------"
print poem
print "----------"


five = 10 - 2 + 3 - 6

print "This should give us %s" % five

start_point = 10000

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

beans, jars, crates = secret_formula(start_point)

print "with a starting point of : %d " % start_point
print "We'd have %d beans, %d jars and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it like this way:"
print "We'd have %d beans, %d jars and %d crates" % secret_formula(start_point)