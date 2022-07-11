n=input()
s=[]
for i in n:
    if i.isdigit():
        s.append(int(i))
print(sum(s))        