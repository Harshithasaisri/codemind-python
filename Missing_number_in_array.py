n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    s=a*(a+1)//2
    s2=0
    for i in range(0,len(l)):
        s2+=l[i]
    d=s-s2
    print(d)