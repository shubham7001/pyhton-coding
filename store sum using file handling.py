# Write a program two n.by taking input from a user and save it into a file with the name of sum


f = open("C:\\Users\\maury\\Desktop\\U\\sum.txt","w")
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = a + b
print(c)
f.write("a = "+str(a))
f.write("\tb = "+str(b))
f.write("\tc = "+str(c))
f.close()
