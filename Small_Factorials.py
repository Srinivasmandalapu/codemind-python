def factorial(s):
    f=1
    while(s!=0):
        f=f*s
        s-=1
    return f
n=int(input())
for i in range(n):
    p=int(input())
    print(factorial(p))
