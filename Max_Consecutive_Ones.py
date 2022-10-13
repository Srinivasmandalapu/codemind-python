x=int(input())
nums=list(map(int,input().split()))
k=[]
c=0
for i in nums:
    if i == 1:
        c+=1
    elif(i!=1):
        k.append(c)
        c=0
k.append(c)
print(max(k))