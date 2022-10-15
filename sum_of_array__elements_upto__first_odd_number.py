n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if(i%2!=0):
        break
    else:
        s+=i
print(s)