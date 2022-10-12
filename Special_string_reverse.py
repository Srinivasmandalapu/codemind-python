n=input()
ch=[]
ind=[]
res=[]
for i in range(len(n)):
    if(n[i].isalpha()):
        res.append(n[i])
    else:
        ch.append(n[i])
        ind.append(i)
res=res[::-1]
for i in range(len(ind)):
    res.insert(ind[i],ch[i])
print(*res,sep='')