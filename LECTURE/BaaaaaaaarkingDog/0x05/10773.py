""" 입력
첫번째 줄: 정수 K (1 <= K <= 100,000) 입력
K개의 줄: 0에서 1,000,000 사이의 정수 하나씩 입력
0 입력: 가장 최근에 슨 수 지우기"""
""" 출력
최종적으로 적어낸 수의 합 (<= 2^31-1) 출력"""

import sys
input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    num = int(input())

    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))