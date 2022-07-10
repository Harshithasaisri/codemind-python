n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,len(l)):
    if l[i]==0:
        c=0
    else:
        c+=1
        d=max(d,c)
print(d)