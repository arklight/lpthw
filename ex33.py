prompt = "-->"
in_put = int(raw_input(prompt))

def test_loop(in_put):
    i = 0
    numbers = []
    while i < in_put:
        print "i is %d" % i
        numbers.append(i)

        i  = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    for num in numbers:
        print "numbers are: %d"  % num

test_loop(in_put)
