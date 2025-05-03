import sys
input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(N):
    if arr[i] < x: print(arr[i], end=" ")