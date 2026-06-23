n=1423
numb=n
last=n%10
while numb>=10:
    numb=int (numb/10)

first=numb

print(first+last)