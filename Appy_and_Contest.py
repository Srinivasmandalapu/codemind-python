n=int(input())
for i in range(n):
    m,a,b,k=map(int,input().split())
    c1=m//a
    c2=m//b
    c=m//(a*b)
    if(c1+c2-c>=k):
        print("Win")
    else:
        print("Lose")
