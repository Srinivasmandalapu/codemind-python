s=input()
a=list(s.split())
smax=smin=0
for i in a:
    ma='A'
    mi='z'
    for j in i:
        if ord(j)>ord(ma):
            ma=j
        if ord(j)<ord(mi):
            mi=j
    smax+=ord(ma)
    smin+=ord(mi)
print(smax-smin)