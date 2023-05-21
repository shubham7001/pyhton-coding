# Write a Python program to write a list to a file.

my_list = ['apple', 'banana', 'cherry', 'date']

with open(r"V:\file handling\file02.txt", 'w') as file:
    for item in my_list:
        file.write(item + '\n')
