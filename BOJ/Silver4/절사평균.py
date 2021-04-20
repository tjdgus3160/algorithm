# 6986번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[float(input()) for _ in range(n)]
arr.sort()
print("%.2f"%(sum(arr[k:n-k])/(n-2*k)+1e-9))
print("%.2f"%((sum(arr[k:n-k])+(k*arr[k])+(k*arr[n-k-1]))/n+1e-9))