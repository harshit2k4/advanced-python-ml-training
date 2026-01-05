# in-built functions in python

# math functions
import math
print(math.sqrt(16))
print(math.pi)

print("-------------------")

# random function
import random
random.randint(1,10)
print(random.choice([1,2,3,4,5]))

print("-------------------")
# datetime function
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)