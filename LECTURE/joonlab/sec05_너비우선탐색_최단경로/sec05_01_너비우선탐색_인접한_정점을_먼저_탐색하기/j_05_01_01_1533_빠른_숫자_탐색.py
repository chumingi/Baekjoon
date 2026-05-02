"""
자료구조:
- 정수: (sr, sc) 학생의 현재 위치
- 정수형 배열:
  - A: 보드 정보

알고리즘:
- 배열 A에서 1이 적혀 있는 칸의 정보를 구한다.
- (sr, sc)에서 1이 적혀 있는 칸으로 이동하는 최소 이동 횟수를 구한다.
  - 격자를 정점으로 갖고, 상하좌우로 이웃한 정점끼리 가중치가 없는 간선을 연결한 그래프를 생성한다.
  - (sr, sc) 위치의 칸을 시작 정점으로 한다.
  - 1이 적혀 있는 칸을 도착 정점으로 한다.
  - 시작 정점에서 도착 정점까지의 최단 거리를 너비우선탐색으로 구한다.

"""

from collections import deque


# A: 5x5 크기의 보드 정보가 저장된 2차원 배열
# (sr, sc): 학생의 현재 위치
# 학생이 현재 위치 (sr, sc)에서 시작하여 1이 적혀 있는 칸에 도착하기 위한 최소 이동 횟수를 반환한다.
# 학생이 현재 위치 (sr, sc)에서 시작하여 1이 적혀 있는 칸으로 이동할 수 없는 경우 -1을 반환한다.
def solution(A, sr, sc):
    # 1이 적혀 있는 칸의 위치 (tr, tc)를 구한다.
    tr, tc = 0, 0
    for r in range(5):
        for c in range(5):
            if A[r][c] == 1:
                tr, tc = r, c

    # (sr, sc)에서 (tr, tc)로 이동하기 위한 최소 이동 횟수를 반환한다.
    return get_move_count(A, sr, sc, tr, tc)


# A[sr][sc]에서 A[tr][tc]로 이동하기 위한 최소 이동 횟수를 반환한다.
def get_move_count(A, sr, sc, tr, tc):
    # dd: 상,하/좌/우 이동 시 (행, 열) 변화량을 저장하는 2차원 배열
    # visited[r][c]: (r, c) 위치를 방문한 경우 1을, 방문하지 않은 경우 0 (초깃값)을 저장
    # dist[r][c]: (sr, sc)에서 (r, c)로 이동하기 위한 최소 이동 횟수를 저장
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0] * 5 for _ in range(5)]
    dist = [[0] * 5 for _ in range(5)]

    # q: BFS에 사용할 큐
    # 시작 위치 (sr, sc)를 큐에 넣는다.
    q = deque()
    q.append([sr, sc])

    # A[sr][sc]를 방문했고, 이동 횟수를 0으로 설정한다.
    visited[sr][sc] = 1
    dist[sr][sc] = 0

    # 큐를 이용하여 시작 위치 (sr, sc)에서 도착 위치 (tr, tc)까지 너비우선탐색한다.
    while len(q) != 0:
        # r, c: 큐의 맨 앞에 있는 값을 꺼내서 (r, c)에 저장한다.
        r, c = q.popleft()

        # 목적지에 도달하면 최소 이동 횟수를 반환한다.
        if r == tr and c == tc:
            return dist[r][c]

        # 상, 하, 좌, 우 방향으로 1칸 이동한다.
        for dr, dc in dd:
            # (nr, nc): 다음 이동 위치
            # A[nr][nc]를 아직 방문하지 않은 경우, A[nr][nc]로 이동한다.
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) == True and visited[nr][nc] == 0 and A[nr][nc] != -1:
                q.append([nr, nc])
                dist[nr][nc] = dist[r][c] + 1
                visited[nr][nc] = 1

    # A[tr][tc]에 도달할 수 없는 경우, -1을 반환한다.
    return -1


# (r, c)가 보드 내에 위치하면 True, 아니면 False를 반환한다.
def in_range(r, c):
    return 0 <= r <= 4 and 0 <= c <= 4


A = [list(map(int, input().split())) for _ in range(5)]
sr, sc = map(int, input().split())
print(solution(A, sr, sc))

# 추가 문제: 백준 2178, 2667, 2606, 24444
