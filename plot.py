# Solution to problem 10
# Rebecca Turley, 2019-03-21
# plot.py

# import the module matplotlib.pyplot and bind it to the name plt
import matplotlib.pyplot as plt

import numpy as np

# return evenly spaced values up to 5
x = np.arange(5)

# as I only gave one a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values. (Since python ranges start with 0, the default x vector has the same length as y but starts with 0.)
plt.plot(x, x)

# doubles the values of x
plt.plot(x, 2 * x)

# squares the value of x
plt.plot(x, x * x)

# Create the legends for the graph and place it on the upper left
plt.legend(['y = x', 'y = 2x', 'y = x2', ], loc='upper left')

# give the plot a title
plt.title ("Solution to Problem 10 (hopefully!!)")

# show the graph on the screen
plt.show()





# https://www.wolframalpha.com/input/?i=plot+x,+x%5E2+,+x%5E3++range+0+to+4, https://stackoverflow.com/questions/39923918/plotting-a-line-thats-first-value-is-not-at-x-0
# https://www.youtube.com/watch?v=CuuvojEKHWo, https://matplotlib.org/users/pyplot_tutorial.html