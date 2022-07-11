n=int(input())
l=list(map(int,input().split()))
##print(l)
a=[]
b=[]
m=max(l)##2
for i in range(0,len(l)):
    if l[i]!=m:
        a.append(l[i])##1
sm=max(a)        
if len(a)==0:
    print(m)
else:
    for i in range(0,len(a)):
        if a[i]!=sm:
            b.append(a[i])
if len(b)==0:
    print(m)
else:
    print(max(b))
    