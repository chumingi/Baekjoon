"""
# 아이디어
- 이중 for 문을 돌면서
- 그래프의 값이 1이고 방문하지 않은 경우
- bfs를 돌면서 그림 개수 += 1, 최댓값 갱신

# 시간복잡도
- bfs: O(V + E)
- V: N * M, E: 4V
- N, M <= 500 -> V + E = 5 * 500 * 500 (백만)

# 자료구조
- 그래프 전체 지도: 2차원 배열
- 방문여부: bool 값 2차원 배열
- bfs에서 사용할 큐
"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def bfs(y, x):
    res = 1
    q = deque()
    q.append((y, x))

    while q:
        gy, gx = q.popleft()
        for k in range(4):
            ny = gy + dy[k]
            nx = gx + dx[k]

            if 0 <= nx < m and 0 <= ny < n:
                if map[ny][nx] == 1 and not chk[ny][nx]:
                    res += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return res

cnt = 0
max_V = 0

for y in range(n):
    for x in range(m):
        if map[y][x] == 1 and not chk[y][x]:
            chk[y][x] = True
            cnt += 1
            max_V = max(max_V, bfs(y, x))

print(cnt)
print(max_V)