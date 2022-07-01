def happy(n):
    sq=0
    r=0
    while n>0:
        r=n%10
        sq+=r**2
        n//=10
    return(sq)
a=int(input())
tem=a
while tem!=1 and tem!=4:
    tem=happy(tem)
if tem==1:
    print(True)
else:
    print(False)
        