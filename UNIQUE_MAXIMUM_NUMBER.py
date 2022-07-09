n=int(input())
l=list(map(int,input().split()))
a=[]
x=0
for i in l:
    k=l.count(i)
    if k==1:
        x+=1
        a.append(i)
if len(a)==0:
    print('-1')
else:
    print(max(a))