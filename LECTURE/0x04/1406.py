""" 입력
첫째 줄: 초기에 편집기에 입력되어 있는 문자열이 입력
문자열은 길이(N): 영어 소문자로만 구성, (N <= 100,000)
둘째 줄: 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000) 입력
셋째 줄부터 M개의 줄: 입위의 네 가지 중 하나의 명령어를 순서대로 입력"""
""" 출력
첫째 줄: 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력"""

import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
M = int(input())


for _ in range(M):
    cmd = input().strip()
    if cmd == "L":
        if left:
            right.append(left.pop())
    elif cmd == "D":
        if right:
            left.append(right.pop())
    elif cmd == "B":
        if left:
            left.pop()
    else:
        P, S = cmd.split()
        left.append(S)
print(''.join(left + right[::-1]))

""" 시간복잡도: O(N + M)
- M: 명령어 개수 (최대 500,000)
- 각 명령어 처리에서 사용하는 연산:
    - pop(), append() → 평균 O(1)
    - split() → O(1)
- right[::-1]은 마지막에 한 번만 수행되며 길이 최대 100,000 → O(N)
- 따라서 전체 시간복잡도는 O(N + M)"""
""" 공간복잡도: O(N + M)
- left와 right 리스트에 최대 N + M 개의 문자가 저장될 수 있음
- 추가 문자열 입력 없이 리스트 연산만 수행하므로 O(N + M)"""