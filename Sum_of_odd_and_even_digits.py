n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(0,len(l)):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
d=abs(o-e)
if d==0:
    print("YES")
else:
    print("NO")