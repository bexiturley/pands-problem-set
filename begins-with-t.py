# Solution to problem 2
# Rebecca Turley, 2019-02-18
# beginswitht.py

import datetime

now = datetime.datetime.now().strftime("%A")

print (now)
if now == "Tuesday":
    print ("Yes - today begins with a t") 
elif now == "Thursday":
    print ("Yes - today begins with a t")
else:
    print ("No - today does not begin with a t ")






