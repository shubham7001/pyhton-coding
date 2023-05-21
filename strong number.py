n = int(input('enter the numebr : '))
temp = n
sum = 0
while(n>0):
    rem = n%10
    fact  = 1
    for i in range(1,rem+1,1):
        fact *=i
    sum += fact
    n = n//10
if(sum == temp):
    print('strong number ')
else:
    print('not strong number ')
    
