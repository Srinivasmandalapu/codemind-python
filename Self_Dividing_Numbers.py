n=int(input())
m=int(input())
def is_fun(s):
    c=0
    l=0
    t=s
    while(s!=0):
        d=s%10
        s=s//10
        c+=1
        if(d!=0 and t%d==0):
            l+=1
    if(c==l):
        return 1
    else:
        return 0
for i in range(n,m+1):
    if(is_fun(i)):
        print(i,end=" ")