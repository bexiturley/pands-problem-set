# Solution to problem 3
# Rebecca Turley, 2019-02-13
# python divisors.py

# This prints out all numbers between 1000 and 10000 that are divisible by 6 but not 12


# x is a number in the range of 1000 (that is greater than) and 10000 (less than)
for x in range (1000, 10000) :

# the numbers are divisible by 6 but not (!) by 12.  The and (logical operator) between both of them indicate that both parts of the conditions have to be met not just one, which would be shown by or.
    if (x % 6 == 0)  and (x % 12 != 0) :

# print to the screen all the numbers that meet the above conditions, and in a horizontal format (it makes them easier to see rather than scrolling for pages and pages down)
       print(x, end=' ')
       

#I looked at the following websited and adapted some code from them:  http://www.openbookproject.net/thinkcs/python/english2e/ch04.html, https://www.pythoncentral.io/pythons-range-function-explained/, https://docs.python.org/3.7/tutorial/index.html
