n=int(input())
p=0
q=0
def is_palindrome(s):
    rev=0
    d=0
    t=s
    while(s!=0):
        d=s%10
        s=s//10
        rev=rev*10+d
    if(t==rev):
        return 1
    else:
        return 0
for i in range(n-1,0,-1):
    if(is_palindrome(i)):
        p=i
        break
for i in range(n+1,10000):
    if(is_palindrome(i)):
        q=i
        break
if(abs(p-n)>abs(q-n)):
    print(q)
elif(abs(p-n)==abs(q-n)):
    print(p,q)
else:
    print(p)