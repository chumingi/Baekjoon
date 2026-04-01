"""
자료구조:
- 정수형 배열:
  - board: 보드 정보를 저장
  - aloc: 학생의 현재 위치

알고리즘:
- 현재 위치 aloc에서 상/하/좌/우 방향으로 이동하여 사과를 3개 먹을 수 있는지 확인한다.
- 먹을 수 있는 방향은 모두 이동해 보고, 이 중에서 최소 이동 횟수를 반환한다.
- 상/하/좌/우 방향으로 이동할 때, 현재 위치를 장애물로 변경하여 재귀함수를 호출하고, 재귀함수가 종료되면 원래 값으로 변경한다.
"""


# board: 5x5 크기의 보드 정보를 나타내는 2차원 배열
# aloc: 학생의 현재 위치 (행번호, 열번호)를 나타내는 1차원 배열
# 학생이 현재 위치에서 사과 3개를먹기 위한 최소 이동 횟수를 반환한다.
# 현재 위치에서 사과 3개를 먹을 수 없으면 -1을 반환한다.
def solution(board, aloc):
    # board: 보드의 초기 상태
    # aloc: 학생의 현재 위치
    # 3: 앞으로 먹어야 할 사과 개수
    return solve(board, aloc, 3)


# board: 보드의 현재 상태, aloc: 학생의 현재 위치
# apple_num: 앞으로 먹어야 할 사과 개수
# 현재 위치 aloc에서 apple_num개 사과를 먹기 위한 최시ㅗ 이동 횟수를 반환한다.
# apple_num개의 사과를 먹을 수 없는 경우 -1을 반환한다.
def solve(board, aloc, apple_num):
    # 사과를 모두 먹은 경우, 추가 이동이 필요 없다.
    if apple_num == 0:
        return 0

    # ret: 현재 위치 aloc에서 apple_num개 사과를 먹기 위한 최소 이동 횟수 (초깃값: -1)
    ret = -1

    # 상/하/좌/우 방향으로 모두 시도해 본다.
    # dd: 상/하/좌/우 이동 시 (행, 열) 변화량
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dr, dc in dd:
        # (r, c): 다음 위치
        # (r, c) 위치에 장애물이 없는 경우, (r, c) 위치로 이동한다.
        r, c = aloc[0] + dr, aloc[1] + dc
        if in_range([r, c]) and board[r][c] != -1:
            # 현재 위치에 있는 값을 prv_value에 저장한 후,
            # 현재 위치를 장애물로 변경한다.
            prv_value = board[aloc[0]][aloc[1]]
            board[aloc[0]][aloc[1]] = -1

            # 다음 이동 위치인 (r, c)로 이동한다.
            # (r, c)로 이동하여 apple_num개의 사과를 먹을 수 있는 경우,
            # 현재의 1회 이동을 cur_ret에 반영한다.
            cur_ret = solve(board, [r, c], apple_num - board[r][c])
            if cur_ret != -1:
                cur_ret += 1

            # 정답을 갱신한다.
            if cur_ret != -1:
                if ret == -1 or cur_ret < ret:
                    ret = cur_ret
            # 현재 위치를 이전 값으로 원상복귀시킨다. (back-tracking)
            board[aloc[0]][aloc[1]] = prv_value

    # 정답을 반환한다.
    return ret


# (loc, loc[1]) 위치가 board 안에 위치하면 True, 아니면 False를 반환한다.
def in_range(loc):
    return 0 <= loc[0] <= 4 and 0 <= loc[1] <= 4


board = [list(map(int, input().split())) for _ in range(5)]
aloc = list(map(int, input().split()))
print(solution(board, aloc))

# 추가 문제: 백준 11729
