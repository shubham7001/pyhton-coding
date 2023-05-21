# Write a Python program to read first n lines of a file

'''f = open(r"C:\Users\maury\Desktop\file handling\vedanshu.txt","w")
f.write("India is famous for its ancient history,\n")
f.write("varied landscapes and diverse culture.\n")
f.write("Mark Twain, a celebrated American author,\n")
f.write("once said: India is the cradle of the human race,\n")
f.write("the birthplace of human speech, the mother of history,\n")
f.write("the grandmother of legend and the great-grandmother of tradition.\n")
f.close()'''
f = open("vedanshu.txt","r")
print(f.readline(3))
