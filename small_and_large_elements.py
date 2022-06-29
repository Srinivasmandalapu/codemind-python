s=input()
a=list(s.split())
x=c=0
ma='z'
mi='A'
for i in a[0]:
    if ord(i)<ord(ma):
        ma=i
        for i in a[len(a)-1]:
            if ord(i)>ord(mi):
                mi=i
print(ma,mi)