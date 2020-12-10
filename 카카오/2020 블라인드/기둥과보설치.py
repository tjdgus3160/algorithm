# hint: 2차원 좌표에 기둥,보 각각 설치 여부를 담도록 4좌표계 생성
# 설치 검사 여부를 가지고 삭제시 삭제후 설치 검사 여부 재사용

def solution(n, build_frame):
    def init(n):    # n+1 x n+1 배열 만들기
        res=[]
        for i in range(n+1):    # y축
            tmp=[]
            for j in range(n+1):    # x축
                tmp .append([j,i,0,0]) # (x,y,기둥,보)
            res.append(tmp)
        return res
    def check(block,x,y):
        res=True
        if block[y][x][2]==1:   # 기둥
            if y==0 or block[y-1][x][2]==1 or block[y][x][3]==1 or (x>0 and block[y][x-1][3]==1):
                res=True
            else:
                return False
        if block[y][x][3]==1:
            if (y>0 and block[y-1][x][2]==1) or (y>0 and block[y-1][x+1][2]==1) or (x>0 and x<n and block[y][x-1][3]==1 and block[y][x+1][3]==1):
                res=True
            else:
                return False
        return res

    block=init(n)
    for i in build_frame:
        x,y,typ,act=i
        if act==1:  # 설치
            if typ==0:  # 기둥
                block[y][x][2]+=1
                if check(block,x,y) is False:
                    block[y][x][2] -= 1
            else:   # 보
                block[y][x][3] += 1
                if check(block, x, y) is False:
                    block[y][x][3] -= 1
        else:   # act == 0 삭제
            if typ==0:  # 기둥
                if block[y][x][2]:
                    block[y][x][2]-=1
                if(check(block,x,y) and check(block,x,y+1) and check(block,x-1,y+1)) is False:
                    block[y][x][2]+=1

            else:   # 보
                if block[y][x][3]:
                    block[y][x][3]-=1
                if (check(block,x,y) and check(block,x-1,y) and check(block,x+1,y)) is False:
                    block[y][x][3]+=1
    answer=[]
    for i in range(len(block)):
        for j in range(len(block)):
            if block[j][i][2]:
                answer.append([block[j][i][0],block[j][i][1],block[j][i][2]-1])
            if block[j][i][3]:
                answer.append([block[j][i][0],block[j][i][1],block[j][i][3]])
    return answer

n=5
build_frame=[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n,build_frame))