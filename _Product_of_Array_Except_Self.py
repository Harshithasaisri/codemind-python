n=int(input())
l=list(map(int,input().split()))
for i in l:
    p=1
    for j in l:
        if i!=j:
            p*=j
    print(p,end=' ')    