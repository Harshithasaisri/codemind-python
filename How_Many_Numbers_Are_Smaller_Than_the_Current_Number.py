n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    s=0
    for j in range(0,len(l)):
        if l[j]<l[i]:
            s+=1
    print(s,end=' ')    