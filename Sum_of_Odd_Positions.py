n=int(input())
l=list(map(int,input().split()))
oc=0
for i in range(0,len(l)):
    if i%2!=0:
        oc+=l[i]
print(oc)