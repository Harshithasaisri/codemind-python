n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(l)-1,(n//2)-1,-1):
    a.append(l[i])
for i in range(0,len(l)//2):
    b.append(l[i])
c=a+b
print(*c)