# 나의 풀이
from bisect import bisect_left, bisect_right


def solution(n, m, A, B):
    answer = []
    A.sort()

    for b in B:
        i = bisect_left(A, b[0])
        j = bisect_right(A, b[1])
        answer.append(j - i)
    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)

# 교재 풀이
"""
자료구조:
- 정수: n, m
- 정수형 배열: A, B

알고리즘:
- 이진탐색을 위해 배열 A를 오름차순으로 정렬한다.
- 배열 B에 저장된 모든 질의 b_i를 순서대로 탐색한다.
- 배열 A의 원소 중, i보다 크거나 같고, j보다 작거나 같은 원소의 개수를 이진탐색으로 구한다.
  - 파이썬의 bisect_left(), bisect_right() 함수를 이용한다.
"""

# n, A: n개의 정수가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
# bisect_left(), bisect_right() 함수 사용
from bisect import bisect_left, bisect_right


def solution(n, m, A, B):
    # 배열 A를 오름차순으로 정렬한다.
    A.sort()

    # m개의 질의를 순서대로 처리한다.
    answer = []
    for i, j in B:
        x, y = bisect_left(A, i), bisect_right(A, j)
        answer.append(y - x)

    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)

# 추가 문제: 백준 10816
