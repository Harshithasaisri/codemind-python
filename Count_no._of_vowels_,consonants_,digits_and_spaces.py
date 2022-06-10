n=input()
c=0
d=0
e=0
f=0
for i in n:
    if i==' ':
        c+=1
    elif i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='9' or i=='7' or i=='8' :
        f+=1
    elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        d+=1
    else:
        e+=1
print('Vowels:',d)
print('Consonants:',e)
print('Digits:',f)
print('White spaces:',c)