arr=[1,0,2,3,4,5,6,7,8,9]
large=arr[0]
secondLarge=arr[0]
for i in range(0,len(arr),1):
    if i>large:
        secondLarge=large
        large=i
    elif i<large and i>secondLarge:
        secondLarge=i

print("Largest:",large)
print("Second Largest:",secondLarge)
