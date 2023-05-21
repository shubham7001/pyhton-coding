import random 
user = int(input("enter the number"))
c = random.randrange(1,501)
print(c)
if(user == c):
    print("value is equal")
elif(user>c):
    print("user number is greater than computer number")
else:
    print("user number is less than computer")
