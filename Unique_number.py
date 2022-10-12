n=int(input())#22
temp=n
l=[]
c=0
k=0
while(n>0):
    c=c+1
    r=n%10
    if(r in l):
        break
    else:
        k=k+1
        l.append(r)
        n=n//10
if(c==k):
    print("Unique Number")
else:
    print("Not Unique Number")