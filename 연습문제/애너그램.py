# 애너그램: 문장 또는 단어의 철자 순서를 바꾼것
# 문자열 안의 문자와 갯수가 같으면 True

# 카운터 사용
from collections import Counter
def find(s1,s2):
    cnt=Counter()
    for i in s1:
        cnt[i]+=1
    for i in s2:
        cnt[i]-=1
    for i in cnt.values():
        if i:
            return False
    return True

# 해시 함수 속성 사용
import string
def findhash(s):
    k=0
    for i in s:
        if i in string.whitespace:  # 공백 제거
            continue
        k=k+ord(i)
    return k

s1="marina"
s2="aniram"
print(find(s1,s2))
print(True if findhash(s1)==findhash(s2) else False)