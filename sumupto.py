# Solution to problem 1
# Rebecca Turley, 2019-10-18
# Sumupto.py

# Asks the user to enter a number, then outputs the total of all the numnbers between one and the inputted number


# Set n, the number to be entered, as an integer. Any thing other than a positive integer will result in an error message and the programme not running correctly.  
# When the program is run a message appears asking the user to input a positive integer (number)
n = int(input("Please enter a positive integer: "))

# Assigns a new value to n, equal to the previous value of n plus 1 which was entered by the user at the start. The formula is similar to arithmetic progression which I looked up on https://www.math10.com/en/algebra/arithmetic-progression.html to help me understand how to define the problem before I could start to code it.
ans = (n*(n + 1))/2

Exception ValueError:
    print "Invalid Input. Try again: "

# The above formula gives an answer (ans). Below the programme instructed to print the answer to the screen.
print(ans)

#  looked at the following websites and adapted some code from them: https://www.youtube.com/watch?v=rfscVS0vtbw, https://www.quora.com/What-is-the-sum-of-the-numbers-from-1-to-20 and https://docs.python.org/3.7/tutorial/index.html


#Ignore below, its just additional code I want to try and get working to output different error messages if the wrong types of values are entered. 
#try:
#            if int < 0:  # if not a positive integer print message and ask for input again
#      print("Input must be a positive integer, try again")
#            continue
#        break
#    except ValueError:
#        print("That is not an integer")  