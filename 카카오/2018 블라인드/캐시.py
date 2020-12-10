# LRU 구현 방식 주의
# 페이지 히트시 그 값을 맨 뒤로 옮겨주어야함
# 페이지 폴트시 맨 앞에 값을 뺀다

input=[[3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
       [3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
       [2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
       [5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
       [2,["Jeju", "Pangyo", "NewYork", "newyork"]],
       [0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]]
output=[50,21,60,52,16,25]

def find(n,city):
    city = list(map(lambda a : a.lower(), city))
    cach = []
    cnt = 0
    time = 0
    if n==0:
        return 5*len(city)
    for i in range(len(city)):
        # 페이지 폴트
        if city[i] not in cach:
            if cnt<n:
                cach.append(city[i])
                cnt+=1
            else:
                del cach[0]
                cach.append(city[i])
            time+=5
        # 페이지 히트
        else:
            del cach[cach.index(city[i])]
            cach.append(city[i])
            time+=1
    return time
print(find(input[4][0],input[4][1]))