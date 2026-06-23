
arr=[1,0,2,3,4,5,6,7,8,9]
max=arr[0]
min=arr[0]
for i in range(1,len(arr),1):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]

print("Max Element:",max)
print("Min Element:",min)