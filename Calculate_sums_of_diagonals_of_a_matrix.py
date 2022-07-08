n=int(input())
r=0
c=0
for i in range(0,n):
    a=list(map(int,input().split()))
    for j in range(0,n):
        if i==j:
            r+=a[j]
        if i+j==n-1:
            c+=a[j]
print('Principal Diagonal:',end='')
print(r)
print('Secondary Diagonal:',end='')
print(c)