n=int(input())
d="1234567890"
for i in range(n):
    p=input()
    c=0
    for i in p:
        if(i in d):
            c+=1
    if(c==len(p)):
        print("True")
    else:
        print("False")