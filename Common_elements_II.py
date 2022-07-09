n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
for i in l1:
    if i not in l2:
        if i not in a:
            a.append(i)
for i in l2:
    if i not in l1:
        if i not in a:
            a.append(i)            
print(*a)            