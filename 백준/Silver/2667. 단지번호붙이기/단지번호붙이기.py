"""
# 아이디어
- 이중 for문을 돌다가
- 만약 값이 1이고 방문하지 않았다면 dfs
- dfs를 통해 찾은 값을 저장한 후 정렬

# 시간복잡도
- O(V + E)
- V: n*n, E: 4*n*n
- n <= 25, 25*25 = 625 < 2억

# 자료구조
- 그래프를 저장할 int값 2차원 배열
- 방문여부를 저장하는 bool값 2차원 배열
- 결과값을 저장할 int 리스트
"""

import sys
input = sys.stdin.readline

n = int(input().strip())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < n:
            if map[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                dfs(ny, nx) # 재귀 호출

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and not chk[j][i]:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)
result.sort()

print(len(result))
for i in result:
    print(i)