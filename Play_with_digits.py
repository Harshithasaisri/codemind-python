n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    while(i):
        d=i%10
        c+=d
        i//=10
print(c)