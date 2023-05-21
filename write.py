'''f = open(r"V:\FILE HANDLING\file01.txt","a")
f.write("my self vedanshu maurya\n")
f.close()'''

f = open("file01.txt","r")
p = f.readlines()
for i in range(5):
    print(p[i])

    



