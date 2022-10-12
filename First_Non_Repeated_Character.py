n=int(input())
for i in range(n):
    p=int(input())
    s=input()
    c=0
    f=0
    for i in s:
        c=0
        for j in s:
            if(i==j):
                c+=1
        if(c==1):
            f=1
            z=i
            break
    if(f==0):
        print("-1")
    else:
        print(z)