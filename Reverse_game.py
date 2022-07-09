def pal(n):
    s=str(n)
    s=s[::-1]
    s=int(s)
    return s
n=int(input())
k=list(map(int,input().split()))
for i in range(len(k)):
    k[i]=pal(k[i])
print(*k)