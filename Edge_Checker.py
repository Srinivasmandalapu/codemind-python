n,m=map(int,input().split())
for i in range(10):
    if(i==n and i+1==m or i==m and i+1==n or n==1 and m==10 or n==10 and m==1):
        print("Yes")
        break
else:
    print("No")