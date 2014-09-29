def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#updated
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# take 1 arg
def print_one(arg1):
    print "arg1: %r:" % arg1

def print_none():
    print "I got nothing"

print_two("Brandon","Freeman")
print_two_again("B","Free")
print_one("Second!")
print_none()
