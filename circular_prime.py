n=int(input())
c=0
s=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        break
else:
    c=c+1
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
for i in range(2,(s//2)+1):
    if(s%i==0):
        break
else:
    c=c+1
if(c==2):
    print("circular prime")
elif(c==1):
    print("prime but not a circular prime")
else:
    print("not prime")
    