#/usr/bin/env python

print "You enter a room with two doors. What door will you choose?"

prompt = "-->"
door = raw_input(prompt)

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the beast"

    bear = raw_input(prompt)

    if bear == "1":
        print "The bear eats your face off. You Die!"
    elif bear == "2":
        print "The bear eats your legs off. You live!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss."
    print "1. Eat Blueberries."
    print "2. Smile and walk in."
    print "3. understanding revolvers yelling melodies."

    insanity = raw_input(prompt)

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello."
    else:
        print "The insanity rots your eyes into a pool of muck!"

else:
    print "YOU BROKE IT"
