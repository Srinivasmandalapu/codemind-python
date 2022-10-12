n=input()
c=1
count=0
for i in range(len(n)-1):
    if(n[i]==n[i+1]):
        c+=1
    else:
        if(count<c):
            count=c
        c=1
if(count<c):
    count=c
print(count)