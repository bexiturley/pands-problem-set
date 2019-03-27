# Solution to problem 8
# Rebecca Turley, 2019-02-13
# python datetime.py



# import the current date and time
import datetime

# the exact date and time in the selected format
now = datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p")

# print the selected format to the screen
print (now)

# I looked at the following websites and adapted some code from them: https://www.pythonforbeginners.com/basics/python-datetime-time-examples,  https://www.w3schools.com/python/python_datetime.asp, https://www.youtube.com/watch?v=rfscVS0vtbw, https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-python/28189527 and https://docs.python.org/3.7/tutorial/index.html
# I had an issue with problem 2 as I originally saved this file as datetime.py. When I went to run problem 2 (who also imports date time), it tried to import the results of this file which caused an error message so I amended the title of the problem to the number.
# I couldnt figure out what the problem was for ages. I tried updating on github but made a complete mess of things. I had to scrap the original repository and start again.  This is the link to the one I scrapped (https://github.com/bexiturley/pands-problem-set-fail) It was very fustrating until I figured it out.
# But I see it was a really good troubleshooting experience and I got more practice using github.