def fun(n):
    if(n==1):
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
                break
        return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(fun(i)):
        c+=1
print(c)