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
def is_rev(s):
    rev=0
    d=0
    while(s!=0):
        d=s%10
        s=s//10
        rev=rev*10+d
    return rev
if(is_prime(n)):
    p=is_rev(n)
    if(is_prime(p)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    