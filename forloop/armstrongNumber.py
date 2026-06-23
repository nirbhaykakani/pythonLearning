def countDigits(n):
    num=n
    count=0
    while(num>0):
        count=count+1
        num=int(num/10)
    
    return count

sum=0
n=153
count=countDigits(n)
numb=n
while numb>0:
    sum=sum+(numb%10)**count
    numb=int(numb/10)

if n==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")