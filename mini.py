# Creating random password:

import random
import string

data = string.printable
val = random.choice(data)

password = ""
i = 0
while i < 12:
    val = random.choice(data)
    password = password + val
    i = i + 1
print("Your random password is:",password)

