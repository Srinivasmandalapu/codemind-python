n=input()
c=[]
for i in n:
    if(i.isalpha()):
        c.append(i)
k=0
c.sort()
for i in n:
    if(i.isalpha()):
        print(c[k],end="")
        k+=1
    else:
        print(i,end="")
print(end=" ")