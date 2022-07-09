a,b=map(int,input().split())
k=list(map(int,input().split()))
c=0
for i in range(len(k)):
    if(k[i]%b==0):
        c+=1
print(c)