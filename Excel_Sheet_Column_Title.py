n=int(input())
t=""
while(n):
    r=n%26
    if r==0:
        t+='z'
    else:
        t+=chr(64+r)
    n/=26
    n=int(n)
print(t[::-1])