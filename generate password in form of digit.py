#Write a program to generate password with a fixed length

import random
lower = int(input("enter the lower range : "))
upper = int(input("enter the upper range : "))
password = random.randint(lower , upper)
print("Password is ",password)
