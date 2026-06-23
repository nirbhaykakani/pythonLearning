arr=[-1,0,-2,-3,4,5,6,7,8,9]
negative=0
for i in range(0,len(arr),1):
    if arr[i]<0:
        negative=negative+1
    
print("Negative:",negative)