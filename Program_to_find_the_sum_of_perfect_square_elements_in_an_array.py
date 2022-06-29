import math
def square(a):
    b=int(math.sqrt(a))
    if a==b*b:
        return 1
    else:    
        return 0    
n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    if(square(l[i])):
        sum+=l[i]
print(sum)        
        