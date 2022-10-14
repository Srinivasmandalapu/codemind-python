n=int(input())
l=list(map(int,input().split()))
def is_prime(s):
    if s==1:
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
p=l.index(min(l))
q=l.index(max(l))
c=0
if(p<q):
    for i in range(p,q+1):
        if(is_prime(l[i])):
            c+=1
else:
    for i in range(q,p+1):
        if(is_prime(l[i])):
            c+=1
print(c)