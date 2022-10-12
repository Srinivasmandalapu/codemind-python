n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):
                c+=1
                break
            else:
                break
    print(c)