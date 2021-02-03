# 2082번
import sys
input=sys.stdin.readline

clock={
    0:['###','#.#','#.#','#.#','###'],
    1:['..#','..#','..#','..#','..#'],
    2:['###','..#','###','#..','###'],
    3:['###','..#','###','..#','###'],
    4:['#.#','#.#','###','..#','..#'],
    5:['###','#..','###','..#','###'],
    6:['#..','#..','###','#.#','###'],
    7:['###','..#','..#','..#','..#'],
    8:['###','#.#','###','#.#','###'],
    9:['###','#.#','###','..#','..#']
}
def func(arr):
    for i in range(10):
        for line,s in enumerate(clock[i]):
            for idx in range(3):
                if s[idx]=='.' and arr[line][idx]=='#':
                    break
            else:
                continue
            break
        else:
            return i

h1=[]
h2=[]
m1=[]
m2=[]
for _ in range(5):
    s=input().split()
    h1.append(s[0])
    h2.append(s[1])
    m1.append(s[2])
    m2.append(s[3])
h1=func(h1)
h2=func(h2)
m1=func(m1)
m2=func(m2)
print("%d%d:%d%d"%(h1,h2,m1,m2))
