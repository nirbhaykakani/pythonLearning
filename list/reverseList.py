arr=[1,2,3,8,4,5,6,7,8,9]

left=0
right=len(arr)-1
while(left<right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    left=left+1
    right=right-1

print(arr,end=" ")