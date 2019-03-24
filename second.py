# Solution to problem 9
# Rebecca Turley, 2019-03-24
# second.py

# contains the command-line arguments passed to the script
#import sys
#print (sys.argv)




import csv
# returns the specific way the script was called
from sys import argv
# python will import os to determine which module to load for path
import os.path

# with the file moby-dick open in the read format
with open ('moby-dick.txt', 'r') as f:
    
# loop through the lines of the file (f) 
# enumerate is a function that returns an ordered list on all or some items in a collection. Start on line 1
    for count, line in enumerate(f, start=1):
        # counts every second element (line) and every second element after it
        if count % 2 == 0:
            # print to screen the selected lines
            print(line)

# I used the video you put up https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573, and some of the work I had  previously done on secondstring.py,
# https://docs.python.org/3/library/functions.html#enumerate,https://stackoverflow.com/questions/47062493/how-can-i-get-python-to-read-every-nth-line-of-a-txt-file,  
# https://www.w3schools.com/python/python_conditions.asp, https://stackoverflow.com/questions/8437964/python-printing-horizontally-rather-than-current-default-printing, https://docs.python.org/3/library/stdtypes.html
# I looked at the following websites https://www.youtube.com/watch?v=rfscVS0vtbw and https://www.youtube.com/watch?v=NJSQSbDxyyk.  I also borrowed a lot of code from https://stackoverflow.com/questions/17645327/python-3-3-how-to-grab-every-5th-word-in-a-text-file.