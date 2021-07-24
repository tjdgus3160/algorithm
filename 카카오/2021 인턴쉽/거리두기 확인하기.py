def check(room):
    for y in range(5):
        for x in range(5):
            if room[y][x]=='P':
                # 직선거리 1 확인
                for nx,ny in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if 0<=nx<5 and 0<=ny<5 and room[ny][nx]=='P':
                        return False
                # 직선거리 2 확인
                if 0<=x+2<5 and room[y][x+2]=='P' and room[y][x+1]=='O':
                    return False
                if 0<=x-2<5 and room[y][x-2]=='P' and room[y][x-1]=='O':
                    return False
                if 0<=y+2<5 and room[y+2][x]=='P' and room[y+1][x]=='O':
                    return False
                if 0<=y-2<5 and room[y-2][x]=='P' and room[y-1][x]=='O':
                    return False
                # 대각선 거리 확인
                if 0<=x-1<5 and 0<=y-1<5 and room[y-1][x-1]=='P' and (room[y][x-1]=='O' or room[y-1][x]=='O'):
                    return False
                if 0<=x-1<5 and 0<=y+1<5 and room[y+1][x-1]=='P' and (room[y][x-1]=='O' or room[y+1][x]=='O'):
                    return False
                if 0<=x+1<5 and 0<=y-1<5 and room[y-1][x+1]=='P' and (room[y][x+1]=='O' or room[y-1][x]=='O'):
                    return False
                if 0<=x+1<5 and 0<=y+1<5 and room[y+1][x+1]=='P' and (room[y][x+1]=='O' or room[y+1][x]=='O'):
                    return False
    return True

def solution(places):
    res = []
    for room in places:
        if check(room):
            res.append(1)
        else:
            res.append(0)
    return res

