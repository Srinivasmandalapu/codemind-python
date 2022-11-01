n=int(input())
l=[]
for i in range(1,(n//2)+1):
    for j in range(2,int((i**0.5)+1)):
        if(i%j==0):
            break
    else:
        l.append(i)
c=0        
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]*l[j]==n):
            c=c+1
            print(l[i],l[j])
            break
if(c==0):
    print(-1)
            
            