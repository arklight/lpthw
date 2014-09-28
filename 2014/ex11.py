# take in vars
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

#combind it all
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "Do you want to go another round?",
round_two = raw_input("yes/no: ")

if round_two != "no":
    print "How many dogs do you have?"
    dogs = raw_input('--> ')
    print "What size shoe do you wear?"
    shoe_size = raw_input('--> ')
    print "How many minutes are in an hour?"
    minutes = raw_input('--> ')
    print "You have %r dogs, your shoes are size %r, and you think " \
          "%r is how many minutes are in an hour" % ( dogs, shoe_size, minutes
    )