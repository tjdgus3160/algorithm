def convert(n, base):
    T = "124"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q-1, base) + T[r]

def solution(n):
    return convert(n-1,3)