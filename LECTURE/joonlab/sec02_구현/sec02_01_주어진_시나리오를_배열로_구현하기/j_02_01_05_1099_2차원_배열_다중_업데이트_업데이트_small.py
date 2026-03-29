"""
자료구조:
- 정수: n, m
- 정수형 배열:
  - A: nxn개의 정수가 저장됨
  - B: m개의 질의가 저장됨
알고리즘:
- 배열 B의 모든 원소 b_i를 첫번째 원소부터 m번째 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 b_i에 대해, 질의 b_i를 처리한다.
- 질의 b_i가 유형 1이면,
  - 배열 A의 행번호 i를 i_1부터 i_2까지, 열번호 j를 j_1에서 j_2까지 증가시키면서
  - A[i][j] 원소의 값을 k만큼 증가시킨다.
- 질의 b_i가 유형 2이면,
  - 배열 A의 행번호 i를 i_1부터 i_2까지, 열번호 j를 j_1에서 j_2까지 증가시키면서
  - A[i][j] 원소의 합을 구하고 출력한다.
"""


# n, A: 크기가 nxn인 2차원 배열 A
# m, B: m개의 질의(질의 유형: 1, 2)가 저장된 배열 B
# 유형 2의 질의 결과를 순서대로 한 줄씩 출력한다.
def solution(n, m, A, B):
    # 배열 B에 저장된 m개의 질의를 순서대로 처리한다.
    for b in B:
        if b[0] == 1:
            do_add_query(A, b[1], b[2], b[3], b[4], b[5])
        else:
            print(get_sum(A, b[1], b[2], b[3], b[4]))


# 행 번호 i1 ~ i2, 열 번호 j1 ~ j2에 대해, A의 원소에 k를 더한다.
def do_add_query(A, i1, j1, i2, j2, k):
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            A[i][j] += k


# 행 번호 i1 ~ i2, 열 번호 j1 ~ j2에 대해, A의 원소의 합을 반환한다.
def get_sum(A, i1, j1, i2, j2):
    ret = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            ret += A[i][j]
    return ret


n, m = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
B = list(list(map(int, input().split())) for _ in range(m))
solution(n, m, A, B)

""" 더 생각하기
n = 1,000, m = 300,000으로 매우 큰 경우는 어떻게 할까?
하나의 질의를 처리하는 데 배열 A에 대한 접근이 최대 n**2번 필요하므로
m개의 질의를 처리하는데 최대 m*n**2번의 배열 A 원소 접근이 필요하다.
n = 1,000, m = 300,000이면, n*m**2 = 3*10**11으로 시간 초과가 발생한다.
"""
