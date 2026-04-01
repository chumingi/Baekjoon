"""
자료구조:
- 정수: n

알고리즘:
- 1부터 n-1까지의 합을 재귀 함수로 구한다.
- 앞에서 재귀 함수로 구한 1부터 n-1까지의 합에 n을 더하여 출력한다.
"""

import sys

sys.setrecursionlimit(10**6)


# 1부터 n까지 정수의 합을 반환한다.
def solution(n):
    return solve(n)


# 1부터 n까지 정수의 합을 재귀 함수를 이용하여 구한다.
def solve(n):
    # 종료 조건: n이 1인 경우 1을 반환한다.
    if n == 1:
        return 1

    # 1부터 n-1까지의 합에 n을 더하여 반환한다.
    return n + solve(n - 1)


n = int(input())
print(solution(n))

""" 더 생각하기
반복문을 이용하여 1부터 n까지 정수의 합을 출력하려면 어떻게 해야 할까?
1부터 n까지 반복하면서 정수의 합을 구하면 O(1)에 구할 수도 있다.

# 1부터 n까지 정수의 합을 반복문을 이용하여 반환한다.
def solve(n):
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret

    # 1부터 n까지의 합을 공식을 이용하여 반환한다.
def solve(n):
    return n * (n + 1) // 2
"""

# 추가 문제: 백준 24060
