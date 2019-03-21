# Solution to problem 7
# Rebecca Turley, 2019-03-19
# squareroot.py



#Asks the user to input a number (I used floating integer so 14.5 could be used as an example. I had tried integer and number but they couldnt cope with decimal places)
number =  float (input ("Please enter a positive number "))
# import the math function
import math 
# Print to the screen the message which contains the number the user selected and the result of it, to one decimal place. Using the inbuilt function.
print ('The square root of {} is approx. {:.1f} ' .format(number, math.sqrt (number)))




#https://www.youtube.com/watch?v=L_Ftijam7RE, https://www.tutorialspoint.com/python3/number_sqrt.htm, https://docs.python.org/3.2/library/math.html