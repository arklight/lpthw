i = 0
numbers = []

def for_loop(number_value, add_value):
    i = 0
    for i in range(0, number_value):
        print "At the top i is %d" % i
        numbers.append(i)

        #i += add_value
        print "Numbers now: ", numbers
        print "at the bottom i is %d" % i

for_loop(100, 5)
