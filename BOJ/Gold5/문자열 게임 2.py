# 20437번
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    k = int(input())
    dic = defaultdict(deque)
    short = 10001
    long = 0
    for idx, v in enumerate(s):
        dic[v].append(idx)
        if len(dic[v]) == k:
            short = min(short, dic[v][-1] - dic[v][0] + 1)
            long = max(long, dic[v][-1] - dic[v][0] + 1)
            dic[v].popleft()
    if not long:
        print(-1)
    else:
        print(short, long)