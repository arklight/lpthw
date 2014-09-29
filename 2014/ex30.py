people = 35
cars = 50
trucks = 20

# more cars then print
if cars > people:
    print "We should take the cars."
# more people then cars then print
elif cars < people:
    print "We should not take the cars."
#if all else fails do this
else:
    print "We can't decide."

# more trucks then cars print
if trucks > cars:
    print "That's too many trucks."
# more cars then trucks print
elif trucks < cars:
    print "Maybe we could take the trucks."
# end of the world do this
else:
    print "We still can't decide."

# more people take the trucks
if people > trucks:
    print "Alright, let's just take the trucks."
# game over 
else:
   print "Fine, let's stay home then."
