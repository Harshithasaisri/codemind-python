def vowel(c):
    return(c=='a' or c=='e'or c=='i'or c=='o'or c=='u')
def long_vowel(s):
    r,c=0,0
    for i in range(0,len(s)):
        if vowel(s[i]):
            c+=1
        else:
            r=max(r,c)
            c=0
    return(max(r,c))
n=input()
print(long_vowel(n))