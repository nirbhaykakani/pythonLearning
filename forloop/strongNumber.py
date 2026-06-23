def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i

    return factorial

sum=0
n=150
numb=n

while numb>0:
    sum=sum+factorial(numb%10)
    numb=int(numb/10)

if sum==n:
    print("Strong Number")

else:
    print("Not a Strong Number")