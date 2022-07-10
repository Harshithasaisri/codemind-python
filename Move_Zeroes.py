n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,len(l)):
    if l[i]==0:
        a.append(l[i])
for i in range(0,len(l)):
    if l[i]!=0:
        b.append(l[i])
c=b+a
print(*c)