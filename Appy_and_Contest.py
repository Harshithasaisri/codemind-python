m=int(input())
for i in range(0,m):
    n,a,b,k=map(int,input().split())
    ##print(n,a,b,k)
    c=d=dc=0
    c=n//a
    d=n//b
    dc=n//(a*b)
    if c+d-dc>=k:
        print("Win")
    else:
        print("Lose")