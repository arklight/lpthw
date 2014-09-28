__author__ = 'brandon'
# set value for number of people
x = "There are %d types of people." % 10
# binary value
binary = "binary"
# shorthand
do_not = "don't"
# string replace
y = "Those who know %s and those who %s." % (binary, do_not)

# prints value of x
print x
# outputs value of y
print y
#declare what I said
print "I said: %r." % x
#declare what I said
print "I also said: '%s'." % y

# set to false
hilarious = False
# setup next sentence
joke_evaluation = "Isn't that joke so funny?! %r"

# output values
print joke_evaluation % hilarious

# set more vars
w = "This is the left side of..."
# set more vars
e = "a string with a right side."

# add w and x together
print w + e