n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(0,len(l)):
    sum+=l[i]
print(sum)    