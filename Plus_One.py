n=int(input())
l=list(map(int,input().split()))
r=0
for i in range(len(l)):
    r=r*10+l[i]
r+=1    
s=[]
while r:
    m=r%10
    r=r//10
    s.append(m)
s=s[::-1]
print(*s)
    