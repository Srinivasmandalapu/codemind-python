n=int(input())
l=list(map(int,input().split()))
p=[]
s=0
for i in l:
    if(i not in p):
        p.append(i)
        if(i%2==0):
            s=s+i
print(s)