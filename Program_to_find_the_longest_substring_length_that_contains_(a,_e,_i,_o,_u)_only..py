n=input()
v="aeiou"
c=0
count=0
m=0
for i in n:
    if(i in v):
        c+=1
    else:
        count=c
        if(m<count):
            m=count
        c=0
if(m<c):
    m=c
print(m)