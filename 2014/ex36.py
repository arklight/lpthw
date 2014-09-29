#!/usr/bin/env python

from sys import exit
import random

prompt = "--> "
empty_supply = []
supply = []

def user_interaction():
    print "Choose wisely: Left or Right?"
    choices = raw_input(prompt)
    if choices == "left":
	return left
    elif choices == "right":
	return right
    else:
	print "Clearly you need to read better..."
	#fail back to method you came from
        user_interaction()


def add_supply():
    print "Here is a supply list, take what will help you survive."

    supplies = ['1:belt_buckle', '2:lighter', '3:extra_jacket', '4:walking_cane', '5:gloves', '6:food']
    backpack = []

    for item in supplies:
        print item

    add_supplies = raw_input('add to backback: ')
    print add_supplies

    if add_supplies < 1:
        print "pickup something before you go!"
        print supplies 
        add_supply()
    else:
	supply = backpack.append(add_supplies)
	return start_trouble(supply)

def jungle(supply):
    print "Darkness looms over you."
    print "Two paths lie before you."
    print "Left heads up and seems traveled upon."
    print "Right heads down and seems less traveled upon."

    actions = ['attack', 'flee', 'scream']

    choice = raw_input(prompt)
    if choice == "left":
	print "You run into a jungle cat"
	#print "What are you going to do?"
	#for action in actions:
	#    print action
        print "By some god like strength you slay the beast"
        print "You live out the rest of your days in the jungle"
    elif choice == "right":
	print "You become lost and die"
    else:
	print "You decided to muck around until dark. You have been eaten by wild boar"
	exit(0)

def start_trouble(supply):
    print "\nYour plane crash, it lands between a jungle, winter, and desert area."
    print "What area will you brave?"

    user_action = raw_input(prompt)

    if user_action == "supplies":
        supply = True
	add_supply()
    elif user_action == "jungle":
	jungle(supply)
    elif user_action == "winter":
        print "You are crazy and die because you have no supplies for winter"
        start_trouble(supply)
	#winter(supply, user_action)
    elif user_action == "desert":
        print "You run out of water and die"
        start_trouble(supply)
	#desert(supply, user_action)
    elif user_action == "stop" or "quit" or "exit":
	exit(0)
    else:
	print "You played around to long and died! \n"
	start_trouble(empty_supply)

start_trouble(supply)
