n=int(input())
for i in range(0,n+1):
    x=input()
    c=0
    for i in x:
        if i.isdigit():
            c+=1
    if c>=1:
        print('Yes')
    else:
        print('No')