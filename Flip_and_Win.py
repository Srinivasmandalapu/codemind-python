n=int(input())
s=input()
a=0
i=0
p=0
while i<n-1:
    a+=abs(int(s[i+1])-int(s[i]))
    i+=1
p=n-a-1
if(p%3==0):
    print('Sudhir')
else:
    print('Ashok')