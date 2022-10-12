n=input()
c=0
for i in range(len(n)):
    if(n[i]=="L"):
        c-=1
    if(n[i]=="R"):
        c+=1
    if(n[i]=="U"):
        c+=1
    if(n[i]=="D"):
        c-=1
if(c==0):
    print("True")
else:
    print("False")