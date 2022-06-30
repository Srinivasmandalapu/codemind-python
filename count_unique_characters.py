s=input()
x=len(s)
c=v=u=0
for i in range(x):
    c=0
    if s[i]!=" ":
        for j in range(x):
            if i!=j:
                if s[i]==s[j] or s[i].upper()==s[j] or s[i].lower()==s[j]:
                    c+=1
        if(c==0):
            u+=1
print(u)