n=int(input())
l=list(map(int,input().split()))
ec=0
for i in range(0,len(l)):
    ec+=l[i]
print(ec)