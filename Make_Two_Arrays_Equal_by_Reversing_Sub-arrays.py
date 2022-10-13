n1=int(input())
a1=list(map(int,input().split()))
n2=int(input())
a2=list(map(int,input().split()))
if n1==n2:
    for i in range(n1):
        if a1[i] not in a2:
            print(False)
            break
    else:
        print(True)
else:
    print(True)