n=int(input())
l=list(map(int,input().split()))
ec=0
for i in range(0,len(l)):
    if i%2==0:
        ec+=l[i]
print(ec)