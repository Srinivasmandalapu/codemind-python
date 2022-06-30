s=input()
x=len(s)
c=v=iso=0
for i in range(x):
    c=0
    for j in range(x):
        if i!=j:
            if s[i]==s[j]:
                c+=1
    if(c==0):
        print(s[i])
        iso=2
        break
    else:
        iso=1
if(iso!=2):
    print(-1)