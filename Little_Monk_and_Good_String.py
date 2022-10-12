n=input()
c=0
count=0
v="aeiou"
for i in range(len(n)):
    if(n[i] in v):
        c+=1
    else:
        if(count<c):
            count=c
        c=0
if(count<c):
    count=c
print(count)