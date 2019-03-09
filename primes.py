# Solution to problem 5
# Rebecca Turley, 2019-02-18
# primes.py

# Asks the user to input a positive integer and then tells the user whether or not said number is a prime
# A prime number has no factors except itself and 1. So test from 2 onwards up to the entered number to see if it is a factor of the entered number.


# A message appears on the screen, once the programme is run, asking the user to input a positive integer and sets it as n.  
n = int(input("Please enter a positive integer: "))

# It will cause a loop to start. It checks if the entered number is divisible by 2 and itself. 
for x in range(2, n):
        # if the result of the entered number being divisible by 2 equal to 0  is true then there is no remainder.That means x is a factor of n, and n is not prime.
        if n % x == 0:
            # if there is no remainder, it will print the number to screen stating that it is not a prime
            print(n, 'is not a prime.')
            # A break leaves the innerloop and moves on to the next step of the outer loop
            break
# If the above loop falls through without finding a factor it assumes it is a prime
else:
        # And prints the number to the screen with the message that it is a prime.
        print(n, 'That is a prime.')

# I looked at the following websited and adapted code from them; https://docs.python.org/3/tutorial/controlflow.html, https://docs.python.org/3/library/stdtypes.html, https://stackoverflow.com/questions/26578277/multiple-conditions-with-while-loop-in-python, http://www.openbookproject.net/thinkcs/python/english2e/ch06.html and https://www.youtube.com/watch?v=rfscVS0vtbw.