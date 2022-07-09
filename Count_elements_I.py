n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
s1=set(l1)
s2=set(l2)
#print(s1)
#print(s2)
c=0
for i in s1:
    for j in s2:
        if i==j:
            c+=1
print(c)            