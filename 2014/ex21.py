def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra crdit, type it in anyway.
print "Here is a puzzle"

what = subtract(age, add(height, multiply(weight, divide(iq, 100))))
print "That becomes: ", what, "Can you do it by hand?"

who = add(iq, subtract(age, divide(weight, multiply(height, 15))))
print "magic number: %d" % who


date = add(15, 2)
month = subtract(9, 4)

print "The day is %d and the month is %d" % (date, month)

