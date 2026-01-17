""" 입력
첫째 줄: 입력의 개수 N (1 <= n <= 100,000) 입력
n개의 줄: n 이하의 자연수 하나씩 입력
같은 수가 두 번 나오는 경우는 없음"""
""" 출력
수열을 만들기 위해 필요한 연산을 하나씩 출력
push 연산: + 출력
pop 연산: - 출력
불가능한 경우: NO 출력"""

import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
current = 1

for _ in range(N):
    num = int(input())

    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        current = 0
        break
print("\n".join(result)) if current else print("NO")

""" 시간복잡도: O(N)
- 각 수(1~N)에 대해 push는 **딱 한 번만** 수행
- 각 입력값마다 최대 1번 pop
- 리스트 append/pop은 O(1)
- 총 연산 수: 최대 2N (N번 push + N번 pop) → O(N)"""
""" 공간복잡도: O(N)
- stack: 최대 N개의 수를 저장할 수 있음
- result: 최대 2N개의 문자열 저장 ('+', '-')"""