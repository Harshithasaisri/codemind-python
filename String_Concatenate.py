m=input()
n=input()
k=m+n
l=[k[i] for i in range(0,len(k))]
l.sort()
for i in l:
    print(i,end='')