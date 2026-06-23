arr=[1,11,2,3,4,5,6,7,8,0,9]
even=0
odd=0
for i in range(0,len(arr),1):
    if arr[i]%2==0:
        even=even+1
    else:
        odd=odd+1

print("Even:",even,end=" ")
print("Odd:",odd)