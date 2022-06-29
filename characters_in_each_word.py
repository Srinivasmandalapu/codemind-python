s=input()
v=" "
c=0
for i in s:
    if i in v:
        print(c,end=" ")
        c=0
    else :
        c+=1
print(c)