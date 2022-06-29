s=input()
x=c=0
ma='A'
mi='z'
for i in s:
    if i!=' ':
        if ord(i)>ord(ma):
            ma=i
        if ord(i)<ord(mi):
            mi=i
for i in s:
    if ord(i)==ord(ma):
        c+=1
    if(ord(i)==ord(mi)):
        x+=1
print(mi,x,ma,c)