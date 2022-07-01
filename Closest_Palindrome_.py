def pal(n):
    tem=n
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==tem:
        return(True)
    else:
        return(False)
n=int(input())
h=0
l=0
d=0
for i in range(n+1,n+100):
    if pal(i):
        break
h=i-n
for j in range(n-1,n-100,-1):
    if pal(j):
        break
l=n-j
if h<l:
    print(i)
elif l<h:
    print(j)
elif l==h:
    print(j,i)