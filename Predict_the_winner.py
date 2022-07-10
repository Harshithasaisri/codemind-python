n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
if n%2==0:
    for i in range(0,n//2):
        a.append(l[i])
else:
    for i in range(0,(n//2)+1):
        a.append(l[i])
b=set(l)-set(a)
s1=0
s2=0
for i in a:
    s1+=i
for i in b:
    s2+=i
d=abs(s1-s2)
if d%4==0:
    print('X')
else:
    print('Y')