from sys import argv

print 'name of file that was outputted in last ex'
filename = raw_input()

print "We're going to read %r." % filename
target = open(filename)
print target.read()
target.close()
