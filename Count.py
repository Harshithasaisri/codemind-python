def even(a):
    if a%2==0:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in range(0,len(l)):
    if(even(l[i])):
        ec+=1
    else:
        oc+=1
print(ec,oc)        