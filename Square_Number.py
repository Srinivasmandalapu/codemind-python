n=int(input())
for i in range(1,n):
    if(i*i==n):
        break
if(i*i==n):
    print("True")
else:
    print("False")