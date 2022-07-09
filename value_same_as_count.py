n=int(input())
l=list(map(int,input().split()))
c=0
for i in sorted(set(l),key=l.index):
    if l.count(i)==i:
        c+=1
print(c)