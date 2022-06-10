n=input()
f=0
for i in n:
    if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='9' or i=='7' or i=='8' :
        f+=1
if f!=0:        
    print('Contains',f,'digit')
else:
    print("Doesn't contain digit")
