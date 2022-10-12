p=int(input())
d="1234567890"
c=0
for j in range(p):
    c=0
    n=input()
    for i in n:
        if i in d:
            c+=1
    if(c==0):
        print("No")
    else:
        print("Yes")