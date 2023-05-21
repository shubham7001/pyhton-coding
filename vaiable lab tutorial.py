'''def display():
    global a
    a = 70
    print("inside function call",a)
a = 100
print("before function call ",a)
display()
print("after function call",a)'''




'''#LEGB rule = it is used to nested function
print("LEGB rule")
def display(a):
    a = 70
    print("inside function call",a)
    def d1():
        print("nested function",a)
    d1()
a = 100
print("before function call ",a)
display(a)
print("after function call",a)'''



'''#local varibale
print("local varibale")
def display():
    a = 100
    print("inside function call",a)
    def d1():
        nonlocal a
        a= 70
        print("nested function ",a)
    d1()
    return a
a = 4
print("before function call ",a)
print(display())'''


'''#impiort math
import math
n = int(input("enter the number"))
print(math.sqrt(n))'''

'''#import keyword
import keyword
print(keyword.kwlist)'''


'''#import calender
import calendar
print(calendar.month(2023,4))'''


#import random
import random
print(random.random)


