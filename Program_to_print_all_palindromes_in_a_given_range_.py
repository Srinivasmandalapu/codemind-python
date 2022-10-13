n=int(input())
m=int(input())
def is_palindrome(n):
    temp=n
    rev=0
    d=0
    while(n!=0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if(rev==temp):
        return 1
    else:
        return 0;
temp=0
for i in range(n,m+1):
    if(is_palindrome(i)):
        print(i,end=" ")