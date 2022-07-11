def most_fre(List):
    return max(set(List), key = List.count)
n=int(input())
l=list(map(int,input().split()))
print(most_fre(l))
    
    