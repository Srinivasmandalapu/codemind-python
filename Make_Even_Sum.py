n=int(input())
l=list(map(int,input().split()))
r=0
for i in l:
    r=r+i
if(r%2==0):
    print(1)
else:
    print(0)