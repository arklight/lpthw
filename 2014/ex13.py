from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

round_two = raw_input("Again?(yes/no):")

if round_two != "no":
    a, b, c, d = argv
    print "The letters are:", a
    print "\t and: ", b
    print "\t and: ", c
    print "\t and: ", d

if round_two != "yes":
    car, truck, van, bike = argv
    print "The red one is a:", car
    print "The blue one is a:", truck
    print "The black one is a:", van
    print "The green one is a:", bike