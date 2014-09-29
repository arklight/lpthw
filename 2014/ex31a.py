print "You find yourself running in the woods and stumble upon a fork in the road."
print "Do you go left or right?"

prompt = "--> "
path = raw_input(prompt)

if path == "right":
   print "You walk into the woods and are lost forever"
elif path == "left":
   print "You find a pot of gold laying near a fallen tree"
   print "Do you take it or leave?"

   gold = raw_input(prompt)

   if gold != "leave":
        print "You become sick and die within a minute"
   else:
        print "You wake up and realize this was all a dream"

else:
   print "you have chosen wrongly and death consumes you."
