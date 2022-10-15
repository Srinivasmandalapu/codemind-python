n=int(input())
l=list(map(int,input().split()))
p=[]
s=0
for i in l:
    if(i not in p):
        p.append(i)
        s=s+i
print(s)