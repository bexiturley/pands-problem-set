# Solution to problem 4
# Rebecca Turley, 2019-03-21
# Collatz.py



# The programme invites the user to enter a number.
n = float (input ("Please enter a number "))
  
while n != 1 :
# The condition states that while n (the number entered in the previous step by the user) is not equal to 1 so the steps will be run until 1 is reached.

# print the results of the conditions and statements. I also want a space after the end of the statement instead of a new line character. So all the results will be displayed on the same line.
    print (n,  end=' '),
    if n % 2 == 0:        # n can be divided by 2 so is even
      n = (n / 2)
    else:                 # n is not divisible by 2 so is odd, if this is the case multiply by 3 and add 1.
      n = ((n * 3) + 1)


# I cant get it to print 1 at the end of the answer as I have set the condition to end at 1.  I can not get it to work otherwise. I have tried changing it to less than 1, 0.5. Setting the input as integer rather than a float but to no avail.
# Adapted from code https://stackoverflow.com/questions/41299440/python-how-to-break-while-loop-after-empty-value-in-a-int-turning-input 


