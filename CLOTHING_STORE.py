n=int(input())
arr=list(map(int,input().split()))
c=0
b=set(arr)
p=[]
for i in b:
    p.append(arr.count(i))

for j in range(len(p)):
    c=c+(p[j]//2)
    
print(c)