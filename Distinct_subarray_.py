n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    sum=0
    for j in range(i,m+1):
        sum+=j
        if(sum%2!=0):
            c+=1
print(c)