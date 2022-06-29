a=input()
vow="aeiouAEIOU"
arr=list(a.split())
c=0
for i in arr:
    if i[0] in vow and i[len(i)-1] not in vow:
        c+=1
print(c)