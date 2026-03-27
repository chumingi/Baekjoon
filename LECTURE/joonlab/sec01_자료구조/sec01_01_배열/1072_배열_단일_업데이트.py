"""
자료구조:
- 정수: i, j, k, n
- 정수형 배열: A
알고리즘:
- 배열 A의 원소 A[i]부터 A[j]까지 수넛대로 탐색한다.
- 현재 탐색 중인 원소의 값을 k배 증가시킨다.
- 배열 A의 모든 원소의 합을 구한다.
"""


# n, A: 원소의 개수가 n인 정수형 배열 A
# i, j, k: 배열 A의 i번째 원소부터 j번째 원소에 k를 곱하는 연산 수행
# 연산을 수행한 후 배열 A의 모든 원소의 합을 반환한다.
def solution(n, A, i, j, k):
    # 배열 A의 i번째 원소부터 j번째 원소에 k를 곱하는 연산을 수행한다.
    for idx in range(i, j + 1):
        A[idx] = A[idx] * k
    return sum(A)


# 입력을 받고 정답을 출력한다.
n = map(int, input().split())
A = list(map(int, input().split()))
i, j, k = map(int, input().split())
print(solution(n, A, i, j, k))

# 추가 문제: 백준 11023, 15596, 1292
