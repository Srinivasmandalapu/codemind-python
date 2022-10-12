n=int(input())
while(n>9):
    s=0
    while(n!=0):
        d=n%10
        n=n//10
        s+=d*d
    n=s
if(n==1 or n==7):
    print("True")
else:
    print("False")