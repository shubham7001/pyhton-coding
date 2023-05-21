# Write a Python program to copy the contents of a file to another file


with open(r"V:\file handling\file01.txt",'r') as firstfile, open(r"V:\file handling\file03.txt",'a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # append content to second file
             secondfile.write(line)

		    
