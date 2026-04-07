"""
자료구조:
- 정수: n, m
- 정수형 배열: A, B

알고리즘:
- 이진탐색을 위해 배열 A를 오름차순으로 정렬한다.
- 배열 B에 저장된 모든 질의 b_i를 순서대로 탐색한다.
- 배열 A에서 k보다 큰 원소의 개수를 이진탐색으로 구한다.
  - 파이썬의 bisect_right() 함수를 이용한다.
"""

# n, A: n개의 정수가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
# bisect_right() 함수 사용
from bisect import bisect_right


def solution(n, m, A, B):
    # 배열 A를 오름차순으로 정렬한다.
    A.sort()

    # m개의 질의를 순서대로 처리한다.
    answer = []
    for k in B:
        i = bisect_right(A, k)
        answer.append(n - i)

    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)

# 추가 문제: 백준 2805
