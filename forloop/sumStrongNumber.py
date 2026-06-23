def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i

    return factorial

def strongNumber(n):
    sum=0
    numb=n

    while numb>0:
        sum=sum+factorial(numb%10)
        numb=int(numb/10)

    if sum==n:
        return True

    else:
        return False
    
n=145
sum=0
for i in range(1,n+1):
    if strongNumber(i)==True:
        sum=sum+i

print(sum)