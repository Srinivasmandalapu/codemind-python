n=int(input())
l=list(map(int,input().split()))
p=int(input())
s=0
for i in l:
    s+=i
    if(i==p):
        break
print(s)