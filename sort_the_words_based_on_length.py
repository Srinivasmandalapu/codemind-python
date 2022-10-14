s=list(map(str,input().split()))
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j and len(s[i])<len(s[j]):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
print(*s)