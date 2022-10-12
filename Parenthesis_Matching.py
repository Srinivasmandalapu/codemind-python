n=input()
a=[]
for i in range(len(n)):
    if(n[i]=="(" or n[i]=="{" or n[i]=="["):
        a.append(n[i])
        f=1
    else:
        if(len(n)>0):
            if(a[-1]=="(" and n[i]==")"):
                a.pop()
            elif(a[-1]=="{" and n[i]=="}"):
                a.pop()
            elif(a[-1]=="[" and n[i]=="]"):
                a.pop()
            else:
                print(i+1)
                f=0
                break
        else:
            print(i+1)
            f=0
            break
if(f==1):
    if(len(a)==0):
        print(0)
    else:
        print(len(n)+1)