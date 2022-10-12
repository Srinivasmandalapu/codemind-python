n=input()
d="1234567890"
c=0
for i in n:
    if i in d:
        c+=int(i)
print(c)