"""
자료구조:
- 정수형 배열:
    - board (보드 정보),
    - aloc (학생의 현재 위치),
    - dd (상하좌우 이동 시 (행, 열) 변화량)
 알고리즘:
 - 배열 dd의 모든 방향 d_i를 순서대로 탐색한다.
 - 현재 탐색 중인 d_i에 대해, 학생의 다음 위치에 사과가 있는지 확인한다.
 - 학생의 다음 위치는 현재의 위치 aloc에 현재 방향 d_i의 (행, 열) 변화량을 더하면 된다.
"""


# board: 5x5 크기의 보드 정보를 나타내는 2차원 배열
# aloc: 학생의 현재 위치 (행 번호, 열 번호)를 나타내는 1차원 배열
# 학생이 한 번의 이동으로 사과를 먹을 수 있으면 1을, 먹을 수 없으면 0을 반환한다.
def solution(board, aloc):
    # dd: 상하좌우 이동 시 (행, 열) 변화량
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 상하좌우 방향으로 시도해 본다.
    for dr, dc in dd:
        # (r, c): 다음 이동 위치
        # (r, c) 위치에 사과가 있는 경우 1을 반환한다.
        r, c = aloc[0] + dr, aloc[1] + dc
        if in_range(r, c) and board[r][c] == 1:
            return 1

    # 한 번의 상하좌우 이동으로 사과를 먹을 수 없다.
    return 0


# (r, c)가 board 안에 위치하면 True, 아니면 False를 반환한다.
def in_range(r, c):
    return 0 <= r <= 4 and 0 <= c <= 4


board = list(list(map(int, input().split())) for _ in range(5))
aloc = list(map(int, input().split()))
print(solution(board, aloc))

""" 더 생각하기
상하좌우 방향으로 3번 이하로 이동하여 사과를 2개 이상 먹을 수 있는지 확인할 수 있을까?
위에서는 상하좌우 방향으로 1번 이동하는 경우를 구현했다.
반복문을 이용하여 3번 이동하는 모든 경우를 구현할 수 있다.
"""
