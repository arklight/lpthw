#!/usr/bin/env python

from sys import exit
import random

prompt = "--> "
empty_supply = []

def user_interaction():
    left = "left"
    right = "right"

    choices = raw_input('user_interaction: ')
    if choices == "left":
	return left
    elif choices == "right":
	return right
    else:
	print "choose left or right"
	#fail back to method you came from

def add_supply():
    print "Here is a supply list, take what will help you survive."

    supplies = ['1:belt_buckle', '2:lighter', '3:extra_jacket', '4:walking_cane', '5:gloves', '6:food']
    backpack = []

    for line in supplies:
        print line

    add_supplies = raw_input('add to backback: ')
    print add_supplies

    if add_supplies < 1:
        print "pickup something before you go!"
        print supplies 
        add_supply()
    else:
	new_supply = backpack.append(add_supplies)
	return start_trouble(new_supply)

def jungle(supply):
    print "Darkness looms over you."
    print "Two paths lie before you."
    print "Left heads up and seems traveled upon."
    print "Right heads down and seems less traveled upon."

    action = ['attack', 'flee', 'scream']

    choice = user_interaction()
    if input == "left" in choice:
	print "You run into a jungle cat"
	print "What are you going to do?"
	for line in action:
	    print line
    elif input == "right":
	print "you win"
    else:
	print "broke"
	exit(0)

def start_trouble(supply):
    print "Your plane crash, it lands between a jungle, winter, and desert area."
    print "What area will you brave?"

    user_action = raw_input('start trouble first: ')

    if user_action == "supplies":
	add_supply()
#    elif user_action == "jungle":
#	jungle(supply, user_action)
#    elif user_action == "winter":
#	winter(supply, user_action)
#    elif user_action == "desert":
#	desert(supply, user_action)
    elif user_action == "stop" or "quit" or "exit":
	exit(0)
    else:
	print "You played around to long and died! \n"
	start_trouble(empty_supply)

start_trouble(empty_supply)
