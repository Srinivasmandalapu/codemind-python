n=int(input())
p=0
def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
if(is_prime(n)):
    print("prime")
else:
    print("not a prime")