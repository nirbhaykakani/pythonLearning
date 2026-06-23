def happy(n,count):
    numb=n
    sum=0
    while numb>0:
        digit=int(numb%10)
        sum=sum+digit**2
        numb=int(numb/10)

    count=count+1
    if count>=900:
        return False
    if sum==1:
        return True
    else:
        return happy(sum,count+1)
    
n=71
print(happy(n,0))