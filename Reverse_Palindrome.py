def rev(n):
    s=0
    while(n):
        t=n%10
        s=s*10+t
        n=n//10
    return s

n=int(input())
while(n):
    n+=rev(n)
    if (rev(n)==n):
        print(n)
        break
else:
    print("-1")