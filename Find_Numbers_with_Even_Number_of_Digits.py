n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
    d=0
    while l[i]:
        l[i]//=10
        d+=1
    if d%2==0:
        s+=1
print(s)        