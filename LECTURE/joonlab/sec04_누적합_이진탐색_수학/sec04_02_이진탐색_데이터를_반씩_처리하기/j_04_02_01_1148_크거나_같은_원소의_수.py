"""
자료구조:
- 정수: n, m
- 정수형 배열: A, B

알고리즘:
- 이진탐색을 위해 배열 A를 오름차순으로 정렬한다.
- 배열 B에 저장된 모든 질의 b_i를 순서대로 탐색한다.
- 배열 A에서 k보다 크거나 같은 원소의 개수를 이진탐색으로 구한다.
  - 파이썬의 bisect_left() 함수를 이용한다.
"""

# n, A: n개의 정수가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
# bisect_left() 함수 사용
from bisect import bisect_left


def solution(n, m, A, B):
    # 배열 A를 오름차순으로 정렬한다.
    A.sort()

    # m개의 질의를 순서대로 처리한다.
    answer = []
    for k in B:
        i = bisect_left(A, k)
        answer.append(n - i)

    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)

""" 더 생각하기
bisect_left() 함수를 사용하지 않고 문제를 해결할 수 있을까?
bisect_left(a, k) 함수는 이진탐색을 이용하여 배열 a에서 k보다 크거나 같은 첫번째 원소의 위치를 O(log(n)) 시간에 반환한다.
이진탐색 개념과 lo,mid,hi 변수를 이용하여 bisect_left() 함수와 동일한 기능을 구현해보자.
"""


# n, A: n개의 정수가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
def solution2(n, m, A, B):
    # 배열 A를 오름차순으로 정렬한다.
    A.sort()

    # m개의 질의를 순서대로 처리한다.
    answer = []
    for k in B:
        # 배열 A의 모든 원소가 k보다 크거나 같은 경우, answer에 n을 넣는다.
        if k <= A[0]:
            answer.append(n)
            continue
        # 배열 A의 모든 원소가 k보다 작은 경우, answer에 0을 넣는다.
        elif A[n - 1] < k:
            answer.append(0)
            continue

        # 배열 A에서 k보다 크거나 같은 원소의 수를 계산한다. (이진탐색)
        # - k <= A[i]를 만족하는 가장 작은 i를 찾는다. (0 <= i <= n-1)
        # - A[i-1] < k <= A[i]
        # - A[i..n-1]이 k 이상의 값을 갖는다.
        # 항상 성립하는 조건: k <= A[hi]
        # - hi의 초깃값인 n-1일 때 성립
        # - 왼쪽 또는 오른쪽 부분 탐색 중에도 성립
        lo = 0
        hi = n - 1
        while lo < hi:
            # mid: A[lo] ~ A[hi] 중간 지점
            mid = (lo + hi) // 2

            # k가 왼쪽 부분에 있는 경우, 왼쪽 부분을 추가 탐색한다.
            # k <= A[hi] 조건이 유지된다.
            # A[mid]가 k보다 크거나 같으므로, A[mid+1..hi]에는 정답이 없다.
            if k <= A[mid]:
                hi = mid
            # k가 오른쪽 부분에 있는 경우, 오른쪽 부분을 추가 탐색한다.
            # k <= A[hi] 조건이 유지된다.
            # A[mid]가 k보다 작으므로, A[lo..mid]에는 정답이 없다.
            else:
                lo = mid + 1

        # A[hi..n-1]이 k보다 크거나 같은 값을 갖는다.
        answer.append(n - hi)

    return answer


D = solution2(n, m, A, B)
for d in D:
    print(d)

# 추가 문제: 백준 1654
