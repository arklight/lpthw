print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input('--> ')

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Tale the cake."
    print "2. Scream at the bear."
    print "3. Turn around and run."

    bear = raw_input('--> ')

    if bear == "1":
        print "The bear eats your face off. Game over!"
    elif bear == "2":
        print "The bear mauls you.. you die."
    elif bear == "3":
        print "You run to safty and live!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "What do you do now?"
    print "1. Blueberries."
    print "2. Yellow jacket clothepins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input('> ')

    if insanity == "1" or insanity == "2":
        print "Your body survies powered by a mind of jello."
    else:
        print "The insanity rots your eyes into a pool of muck."

else:
    print "You stumble around and fall on a knife and die."
