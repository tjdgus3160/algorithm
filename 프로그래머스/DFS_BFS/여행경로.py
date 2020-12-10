# hint: dfs중 티켓이 0이되면 옳바른 경로를 찾은것

def dfs(tickets,path):
    if not tickets:
        return path
    for i,ticket in enumerate(tickets):
        if path[-1]==ticket[0]:
            path.append(ticket[1])
            tickets.pop(i)
            tmp=dfs(tickets,path)
            if tmp:
                return tmp
            tickets.insert(i,[ticket[0],ticket[1]])
            path.pop()
    return []

def solution(tickets):
    tickets.sort()
    path=["ICN"]
    dfs(tickets,path)
    return path

arr=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(arr))
