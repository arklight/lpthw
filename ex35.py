#!/usr/bin/env python

from sys import exit

prompt = "--> "

def gold_room():
    print "This room is full of gold bars each weigh 1 pound. How many will you put in your backpack?"

    next = raw_input(prompt)
    if next > 0:
	how_much = int(next)
    else:
	dead("Man, learn to type a number.")

    if how_much < 50:
	print "Nice, you're not greedy, you win!"
	exit(0)
    else:
	dead("You greedy bastard! The gold was posioned and you took to much!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
	next = raw_input(prompt)

	if next == "take the honey":
	    dead("The bear looks at you then slaps your face off.")
	elif next == "taunt bear" and not bear_moved:
	    print "The bear has moved from the door. You can go through it now."
	    bear_moved = True
	elif next == "taunt bear" and bear_moved:
	    dead("The bear gets upset and chews your legs off.")
	elif next == "open door" and bear_moved:
	    gold_room()
	else:
	    print "I got no idea what that means."
	    print "try: taunt bear"
	    print "try: take the honey"


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life, attack the monster, or eat your brains?"
    print "Enter: flee, attack, eat"

    next = raw_input(prompt)

    if "flee" in next:
	start()
    elif "eat" in next:
	dead("Well that was tasty!")
    elif "attack" in next:
	print "You slay the beast!"
	start()
    else:
	cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You enter in a dark room."
    print "There is a door to your right and left."
    print "Which do you choose?"

    next = raw_input(prompt)

    if next == "left":
	bear_room()
    elif next == "right":
	cthulhu_room()
    else:
	print "next time pick a door..."
	dead("You stumble around the room until you starve.")


start()
