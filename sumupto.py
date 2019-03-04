# Solution to problem 1
# Rebecca Turley, 2019-10-18
# Sumupto.py

# Asks the user to enter a number, then outputs the total of all the numnbers between one and the inputted number


# Set n, the number to be entered, as an integer. Any thing other than a positive integer will result in an error message and the programme not running correctly.  
# When the program is run a message appears asking the user to input a positive integer (number)
n = int(input("Please enter a positive integer: "))

# Assigns a new value to n, equal to the previous value of n plus 1 which was entered by the user at the start. The formula is similar to arithmetic progression which I looked up on https://www.math10.com/en/algebra/arithmetic-progression.html to help me understand how to define the problem before I could start to code it.
ans = (n*(n + 1))/2

# The above formula gives an answer (ans). Below the programme instructed to print the answer to the screen.
print(ans)
