import sys
sys.setrecursionlimit(10000000)

def recursionfindroom(room, reservation):
    if room not in reservation:
        reservation[room] = room + 1
        return room
    empty= recursionfindroom(reservation[room], reservation)
    reservation[room]=empty+1
    return empty

def solution(k, room_number):
    answer = []
    reservation = {}
    for i in room_number:
        answer.append(recursionfindroom(i, reservation))
    return answer

k=10
room_number=[1,3,4,1,3,1]
print(solution(k,room_number))
