n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
b=max(l)
for i in range(0,len(l)):
    a.append(b-l[i])
for i in range(0,len(a)):
    if a[i]<=k:
        print('True',end=' ')
    else:
        print('False',end=' ')