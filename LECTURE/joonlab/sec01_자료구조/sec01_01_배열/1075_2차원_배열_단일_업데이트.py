"""
자료구조:
- 정수: n, i1, j1, i2, j2, k
- 정수형 2차원 배열: A
알고리즘:
- 행번호 i를 i부터 i2까지 탐색한다.
- 열번호 j를 j1부터 j2까지 탐색한다.
- A[i][j]의 값을 k배 증가시킨다.
- 행번호 i를 0부터 n-1까지 탐색하면서 모든 행의 원소의 합을 구한다.
"""


def solution(n, A, i1, j1, i2, j2, k):
    answer = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            A[i][j] *= k
    for i in range(n):
        answer += sum(A[i])
    return answer


# 입력을 받고 정답을 출력한다.
n = int(input().split())
A = list(list(map(int, input().split())) for _ in range(n))
i1, j1, k2, j2, k = map(int, input().split())
print(solution(n, A, k1, j1, k2, j2, k))

# 추가 문제: 백준 2440, 2441, 2563
