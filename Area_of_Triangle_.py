import math
p,t,r=map(int,input().split())
s=(p+t+r)/2
area=math.sqrt(s*(s-p)*(s-t)*(s-r))
print("%.2f"%area)