# N줄 N개의 별
N=5
for i in range(N):
    for j in range(N):
        print('*',end='')
    print()

# N줄 직각삼각형 그리기
N=5
for i in range(N):
    for j in range(i+1):
        print('*',end='')
    print()

# 역직각삼각형 그리기
N=5
for i in range(N):
    for j in range(N-i):
        print('*',end='')
    print()

# 이등변삼각형 그리기
N=5
for i in range(N):
    for k in range(N-i-1):
        print(' ',end='')
    for k in range(1+(2*i)):
        print('*',end='')
    print()