n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i!=1 and i!=0:
        s+=1
if s==0:
    print(True)
else:
    print(False)