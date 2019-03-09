# Solution to problem 6
# Rebecca Turley, 2019-02-18
# secondstring.py


# The user is asked to enter a sentence, which is then shortened to x in the programme to simplify working with it (rather than having to use the full sentence each time)
x = input ("Please enter a sentence:  ")


# enumerate is a function that returns an ordered list on all or some items in a collection. 
# split() splits a string into a list
# will be using a integer (i) value to select the location of the words I want to return from the entereed string (s)
# the for loop will go through the whole string 
for i,s in enumerate(x.split()):

  # calculates the remainder of i divided by 2 and prints it to the screen (every alternate word in the entered string)
  if i%2 == 0: 
    print (s, end=' ')

# I found this problem really difficult to try and get my head around so used a lot of websites.  I heavily borrowed most of the code from https://stackoverflow.com/questions/17645327/python-3-3-how-to-grab-every-5th-word-in-a-text-file.
# It was a simple enough matter to adjust it to show the results I wanted but then had to try and understand what I had used and why. (So apologies if my attempt at explaining the code is completely wrong) 
# For this I used the following; https://docs.python.org/3/library/functions.html#enumerate, https://www.w3schools.com/python/python_conditions.asp, https://stackoverflow.com/questions/8437964/python-printing-horizontally-rather-than-current-default-printing, https://docs.python.org/3/library/stdtypes.html
# I looked at the following website https://www.youtube.com/watch?v=rfscVS0vtbw.    
