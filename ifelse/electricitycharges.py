units=300
sum=0
for i in range(1,units+1):
    if i<=50:
        sum=sum+0.50
    elif 51<=i<=150:
        sum=sum+0.75
    else:
        sum=sum+1.20


sum=1.2*sum
print(sum)