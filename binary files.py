import pickle
f = open(r"V:\FILE HANDLING\lab02.txt","br")
'''l = [1,2,3,4,"hello"]
pickle.dump(l,f)
f.close()'''
s = pickle.load(f)
print(s)
f.close()
