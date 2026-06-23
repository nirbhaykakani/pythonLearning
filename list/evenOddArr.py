arr=[1,11,2,3,4,5,6,7,8,0,9]
even=[]
odd=[]
for i in range(0,len(arr),1):
    if(arr[i]%2==0):
        even.append(arr[i])
    else:
        odd.append(arr[i])

print("Even:",even)
print("Odd:",odd)

