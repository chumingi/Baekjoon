"""
자료구조:
- 정수: n, k
- 정수형 2차원 배열: A
알고리즘:
- 배열 A의 모든 원소를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 원소의 값이 k인 원소의 수를 구한다.
"""


# n, A: 크기가 n x n인정수형 2차원배열 A
# 2차원 배열 A의 원소 중에서 값이 k인 원소의 개수를 반환한다.
def solution(n, A, k):
    # 2차원 배열 A의 원소 중에서 값이 k인 원소의 개수를 구한다.
    answer = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                answer += 1
    return answer


# 입력을 받고 정답을 출력한다.
n, k = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
print(solution(n, A, k))

# 추가 문제: 백준 2438, 2439, 2738, 2566
