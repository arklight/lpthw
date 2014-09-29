# import argv method from sys lib
from sys import argv

#pack a few vars from the CLI
script, filename = argv

#set and open the CLI filename
txt = open(filename)

#print out the file that was called
print "Here's your file %r:" % filename
print txt.read()

txt.close()

##prompt for the filename again and print it out
#print "Type the filename again:"
#file_again = raw_input("--> ")

#txt_again = open(file_again)

#print txt_again.read()
