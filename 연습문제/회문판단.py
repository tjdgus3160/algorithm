# 문자열 회문판단, 공백 무시

def is_palindrome(s): # 한방에 비교
    l=s.split(" ")
    s2="".join(l)
    return s2==s2[::-1]

def is_palindrome2(s): # 좌우 끝 문자열 하나씩 비교
    l=len(s)
    f,b=0,l-1
    while f<l//2:
        while s[f]==" ": f+=1
        while s[b]==" ": b-=1
        if s[f]!=s[b]:
            return False
        f+=1
        b-=1
    return True

str1="다시 합창합시다"
str2=""
str3="hello"
print(is_palindrome(str1))
print(is_palindrome(str2))
print(is_palindrome(str3))
print()
print(is_palindrome2(str1))
print(is_palindrome2(str2))
print(is_palindrome2(str3))