import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 12
room = 0

for i in range(N):
    S, Y = map(int, input().split())
    arr[(Y-1)*2 + S] += 1

for j in range(len(arr)):
    room += arr[j] // K
    if arr[j] % K != 0:
        room += 1
print(room)