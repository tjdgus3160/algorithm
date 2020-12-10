import bisect # 정렬된 순서로 list를 유지하고자 할 때 사용
a=[1,3,4,5]

bisect.bisect(a,2) # 정렬된 a리스트에 2가 들어갈 위치를 반환
# bisect_left(arr, x, lo=0, hi=len(arr)): 정렬된 arr리스트의 lo~hi사이에 x가 들어갈 위치 반환
# bisect_right(arr, x): bisect()와 같은 함수
bisect.insort(a,2) # 정렬된 a리스트에 2를 삽입
# insort_left(arr, x) : bisect_left()로 구해진 위치에 x값 삽입

# 이진 탐색: 정렬된 리스트에서 임의의 값 x가 존재하는지 검사
def binary_search(arr, x):
  i = bisect.bisect_left(arr, x)
  return i < len(arr) and arr[i] == x

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
# 리스트 정렬하기
a = []
b = [2,8,1,10,5,4]
for x in b:
  bisect.insort(a, x)

# 점수에 따라 등급 나누기
def get_grade(score):
  r = (50, 60, 70, 90, 100)
  g = 'FDCBA'
  return g[bisect.bisect_right(r, score)]