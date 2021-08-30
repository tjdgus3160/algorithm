from itertools import product

def solution(word):
    alpha=['A','E','I','O','U']
    arr=[]
    for i in range(1,6):
        for sub in product(alpha,repeat=i):
            arr.append(''.join(sub))
    return sorted(arr).index(word)+1