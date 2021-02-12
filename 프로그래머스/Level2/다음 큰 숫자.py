def solution(n):
    s=bin(n)[2:]
    if '01' in s:
        idx = s.rfind('01')
        k=s[:idx]+'10'+''.join(sorted(list(s[idx+2:])))
    else:
        k=s[0]+'0'+''.join(sorted(list(s[1:])))
    return int(k,2)