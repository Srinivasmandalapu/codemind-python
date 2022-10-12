n=input()
l=0
r=0
for i in n:
    if(i=="L"):
        l+=1
    if(i=="R"):
        l-=1
    if(l==0):
        r+=1
print(r)