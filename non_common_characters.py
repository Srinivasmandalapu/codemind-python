s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
p=[]
for i in s2:
    if i not in s1 and i not in p and i!=" ":
        p.append(i)
for i in s1:
    if i not in s2 and i not in p and i!=" ":
        p.append(i)
p=sorted(p)
print("".join(p))