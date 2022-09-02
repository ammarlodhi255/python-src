import sys
import datetime
import calendar
import random
import os
import antigravity 

print(sys.path)

today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now.strftime("%Y/%m/%d"))

print(calendar.isleap(2012))
print(random.choice([1, 2, 3, 2, 12]))

print(os.getcwd())

def printAll(*args):
    print(args)

# printAll("Ammar", "Ahmed", 2)
# print(not None)

# output = "%s %o" % ("Ammar", 8)
# print(output)

# output = "%.2f" % (782.2314)
# print(output)



