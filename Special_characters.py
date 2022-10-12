n=input()
e=[]
o=[]
c=0
for i in n:
    if(i.isalpha()):
        continue
    elif(i.isdigit()):
        if(int(i)%2==0):
            e.append(i)
        else:
            o.append(i)
    else:
        c+=1
if(c%2==0):
    i=0
    j=0
    while(i<len(e) or j< len(o)):
        if(i<len(e)):
            print(e[i],end="")
            i+=1
        if(j<len(o)):
            print(o[j],end="")
            j+=1
else:
    i=0
    j=0
    while(i<len(e) or j< len(o)):
        if(j<len(o)):
            print(o[j],end="")
            j+=1
        if(i<len(e)):
            print(e[i],end="")
            i+=1