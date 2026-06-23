arr=[1,1,2,2,3,5,6,7,8,0,9]
arr1=[]
max=arr[0]
for i in range(0,len(arr),1):
    if arr[i]>max:
        max=arr[i]

for i in range(0,max+1,1):
    arr1.append(0)

for i in range(0,len(arr),1):
    arr1[arr[i]]=arr1[arr[i]]+1

print(arr1)