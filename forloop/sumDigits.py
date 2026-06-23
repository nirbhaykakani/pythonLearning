n=1423
numb=n
sum=0
while numb>0:
    sum=sum+int(numb%10)
    numb=int(numb/10)

print(sum)
