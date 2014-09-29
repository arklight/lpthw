i = 0
numbers = []

def loop(number_value, add_value):
    i = 0
    while i < number_value:
        print "At the top i is %d" % i
        numbers.append(i)

        i += add_value
        print "Numbers now: ", numbers
        print "at the bottom i is %d" % i

loop(100, 5)

print "The numbers: "
for num in numbers:
    print num
