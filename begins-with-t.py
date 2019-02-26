# Solution to problem 2
# Rebecca Turley, 2019-02-18
# beginswitht.py

# this checks to see if today begins with a t, if so a particular message is displayed.  If today does not begin with a t, a different message is displayed.

#import the current date and time
import datetime

#what is the exact date, time and full day of the week
now = datetime.datetime.now().strftime("%A")


#Print to the screen what day of the week is. The full name of the day, not just the first three letters. This wasnt part of the question but I put it in as a double check for myself.
print (now)

#Check today day name (this is obtained from line 9 where the name of the day is imported) against the word Tuesday and if it is the same, print the message, yes-today begins with a t
if now == "Tuesday":
    print ("Yes - today begins with a t") 

#check today name against the word Thursday, if it is the same, print the message, yes-today begins with a t
elif now == "Thursday":
    print ("Yes - today begins with a t")

#if neither of the above statements are true ie. neither day is tuesday or thursday, print no-today does not begin with a t
else:
    print ("No - today does not begin with a t ")

#I looked at the following websites and adapted some code from them: https://www.pythonforbeginners.com/basics/python-datetime-time-examples,  https://www.w3schools.com/python/python_datetime.asp, https://www.youtube.com/watch?v=rfscVS0vtbw, https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-python/28189527 and https://docs.python.org/3.7/tutorial/index.html






