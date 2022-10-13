a=int(input())
b=list(map(int,input().split()))[:a]
if len(set(b))>=3:
    b=list(set(b))
    b.sort()
    b.reverse()
    print(b[2])
else:
    print(max(b))