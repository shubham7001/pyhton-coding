# Write a Python program to count the number of lines in a text file.

num_lines = 0
with open(r"V:\file handling\file01.txt" , 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
