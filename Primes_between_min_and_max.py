def prime(n):
    if n==1:
        return(False)
    for i in range(2,(n//2)+1):
        if n%i==0:
            return(False)
    return(True)
n=int(input())
l=list(map(int,input().split()))
mi=l.index(min(l))
ma=l.index(max(l))
c=0
if mi<ma:
    for i in range(mi,ma+1):
        if prime(l[i]):
            c+=1
else:
    for i in range(ma,mi+1):
        if prime(l[i]):
            c+=1
print(c)        