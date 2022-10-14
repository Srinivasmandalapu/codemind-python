n=input().split()
c=[]
v="aeiouAEIOU"
for j in n:
    c=[]
    for i in j: 
        if(i not in v):
            c.append(i)
    k=0
    c.sort()
    for i in j:
        if(i not in v):
            print(c[k],end="")
            k+=1
        if(i in v):
            print(i,end="")
    print(end=" ")
    