#Write a Python script to generate and print a dictionary that contains a number 
#(between 1 and n) in the form (x, x*x)
# get user input for n
n = int(input("Enter a number: "))
squares = {}
for x in range(1, n+1):
    squares[x] = x*x
print(squares)
