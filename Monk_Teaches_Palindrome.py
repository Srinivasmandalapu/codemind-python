n=int(input())
for i in range(n):
    p=input()
    q="".join(reversed(p))
    if(p==q and len(p)%2==0):
        print("YES EVEN")
    elif(p==q and len(p)%2!=0):
        print("YES ODD")
    elif(p!=q):
        print("NO")