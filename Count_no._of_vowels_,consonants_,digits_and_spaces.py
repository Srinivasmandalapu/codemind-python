n=input()
vc,cc,dc,sc=0,0,0,0
v="aeiou"
d="1234567890"
for i in n:
    if i in v:
        vc+=1
    elif i in d:
        dc+=1
    elif i==" ":
        sc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)