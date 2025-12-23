"""
# 아이디어
- 조건을 만족하지 않으면 break
- while 문으로 조건이 만족하는 동안 반복
- 네 방향 탐색하여 1인 칸 있으면 이동, 없으면 뒤로 1칸 이동
- 뒤로 이동할 수 없으면 종료

# 시간복잡도
- 지도 크기: n*m
- n, m <= 50 -> O(n^2)

# 자료구조
- 전체 지도를 저장하는 배열 (0: 청소 안함, 1: 벽, 2: 청소 함)
- 청소한 칸의 크기 int 변수
- 나의 위치, 방향 int 변수
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1

    sw = False
    for _ in range(4):
        d = (d + 3) % 4
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if map[ny][nx] == 0:
                y, x = ny, nx
                sw = True
                break
    
    if sw:
        continue
    
    by = y - dy[d]
    bx = x - dx[d]

    if not (0 <= by < n and 0 <= bx < m) or map[by][bx] == 1:
        break
    y, x = by, bx

print(cnt)