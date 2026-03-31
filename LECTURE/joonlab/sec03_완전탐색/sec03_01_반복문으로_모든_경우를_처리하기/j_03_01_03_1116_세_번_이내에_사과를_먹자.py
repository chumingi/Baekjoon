"""
자료구조:
- 정수형 배열:
  - board: 보드 정보를 저장
  - aloc: 학생의 현재 위치

알고리즘:
- 학생의 모든 이동 방향을 시도해본다. 첫번째 이동 방향을 i, 두번째 이동 방향을 j, 세번째 이동 방향을 k라고 한다.
- 첫번째 이동 위치 iloc은 aloc에서 i 방향으로 이동한 위치이다.
- 두번째 이동 위치 jloc은 aloc에서 j 방향으로 이동한 위치이다.
- 세번째 이동 위치 kloc은 aloc에서 k 방향으로 이동한 위치이다.
- iloc, jloc, kloc 위치에서 장애물을 피해서 2개 이상의 사과를 먹을 수 있는지 확인한다.
"""


# board: 5x5 크기의 보드 정보를 저장하고 있는 2차원 배열
# aloc: 학생의 현재 위치 (행번호, 열번호)를 저장하고 있는 1차원 배열
# 학생의 현재 위치에서 3번 이하의 이동으로 사과를 2개 이상 먹을 수 있으면 1을, 없으면 0을 반환한다.
def solution(board, aloc):
    # 상/하/좌/우 방향으로 1칸 이동 시, (행, 열) 변화량
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # i: 첫번째 이동 방향, j: 두번째 이동 방향, k: 세번째 이동 방향
    for i in range(4):
        for j in range(4):
            for k in range(4):
                # iloc: 첫번째 이동 위치, jloc: 두번째 이동 위치, kloc: 세번째 이동 위치
                iloc = [aloc[0] + dd[i][0], aloc[1] + dd[i][1]]
                jloc = [iloc[0] + dd[j][0], iloc[1] + dd[j][1]]
                kloc = [jloc[0] + dd[k][0], jloc[1] + dd[k][1]]

                # aloc -> iloc -> jloc -> kloc 순서대로 이동 시
                # 먹을 수 있는 사과 개수가 2개 이상이면 1을 반환한다.
                if get_apple(board, aloc, iloc, jloc, kloc) >= 2:
                    return 1

    # 사과를 2개 이상 먹을 수 없는 경우 0을 반환한다.
    return 0


# aloc -> iloc -> jloc -> kloc 순서대로 이동 시,
# 먹을 수 있는 사과 개수를 반환한다.
def get_apple(board, aloc, iloc, jloc, kloc):
    # 먹을 수 있는 사과 개수를 0으로 초기화한다.
    apple_num = 0

    # 첫번째나 두번째 이동 위치가 보드 밖이면 2개의 사과를 먹을 수 없다.
    if in_range(iloc) == False or in_range(jloc) == False:
        return 0

    # 첫번째나 두번째 이동 위치에 장애물이 있으면 2개의 사과를 먹을 수 없다.
    if board[iloc[0]][iloc[1]] == -1 or board[jloc[0]][jloc[1]] == -1:
        return 0

    # 두번째 위치 jloc가 출발 위치 aloc와 같으면 문제 규칙에 위반된다.
    if aloc == jloc:
        return 0

    # apple_num을 첫번째 위치와 두번째 위치에 있는 사과 개수의 합으로 설정한다.
    apple_num = board[iloc[0]][iloc[1]] + board[jloc[0]][jloc[1]]

    # 세번째 위치의 사과를 apple_num에 반영한다.
    if in_range(kloc) and board[kloc[0]][kloc[1]] == 1 and iloc != kloc:
        apple_num += 1

    return apple_num


# (loc[0], loc[1]) 위치가 board 안에 위치하면 True, 아니면 False를 반환한다.
def in_range(loc):
    return 0 <= loc[0] <= 4 and 0 <= loc[1] <= 4


board = list(list(map(int, input().split())) for _ in range(5))
aloc = list(map(int, input().split()))
print(solution(board, aloc))

# 추가 문제: 백준 2798, 7568
