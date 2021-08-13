input()
arr=[*map(int,input().split())]
res=[i for i in arr if arr.count(i)==1]
print(max(res) if res else -1)