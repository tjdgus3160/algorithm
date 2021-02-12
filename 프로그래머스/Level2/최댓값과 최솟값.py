def solution(s):
    arr=[*map(int,s.split(' '))]
    arr.sort()
    return '%d %d'%(arr[0],arr[-1])