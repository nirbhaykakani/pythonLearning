def prime(n):
    if n==1:
        return False 
    
    is_prime=True

    for i in  range(2,n):
        if n%i == 0:
            is_prime=False
            break

    return is_prime

n=100
sum=0
for i in range(1,101):
    if(prime(i)==True):
        print(i)