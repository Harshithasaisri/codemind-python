n=int(input())
l=list(map(int,input().split()))
s=set(l)
sum=0
for i in s:
    sum+=i
print(sum)    