n=int(input())
a=list(map(int,input().split()))
k=0
b=[]
for i in a:
    if(a.count(i)>k):
        k=a.count(i)
for i in a:
    if(a.count(i)==k):
        b.append(i)
print(min(b))