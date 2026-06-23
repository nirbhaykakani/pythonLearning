n=1423
numb=n
reverse=""
while numb>0:
    reverse=reverse+str(numb%10)
    numb=int(numb/10)

reverse=int(reverse)
print(reverse)

