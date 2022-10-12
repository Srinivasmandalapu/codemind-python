n=input()
c=0
a=0
if(len(n)>20):
    print("No")
else:
    for i in n:
        if(i=="z"):
            c+=1
        else:
            a+=1
if(2*c==a):
    print("Yes")
else:
    print("No")