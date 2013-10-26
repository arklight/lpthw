#!/usr/bin/env python

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
   print "A fruit of type: %s" % fruit

# mixed lists use %r raw input
for i in change:
    print "I got %r" % i

# we can build lists, first start with an empty one
elements = []

# then use a rnage
for i in range(0, 6):
    # append is a function that lists understand
    elements.append(i)
    print "Adding %d to the list." % 1
    print " list is elements.pop(-1) long"

# print the new list of elements
for i in elements:
    print "Element was: %d" % i
