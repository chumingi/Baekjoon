"""
[문제 유형] 스택 / 문자열 / 구현

[핵심 조건]
- 단어 수 n <= 100
- 각 단어 길이 <= 100,000 -> 총 길이 <= 1,000,000 -> o(n * l)까지 가능
- 입력은 a와 b로만 구성된 문자열
- 좋은 단어: 교차 없이 모든 문자가 같은 글자와 정확히 하나씩 짝을 이루는 경우

[풀이 아이디어]
1. 문자를 왼쪽부터 순서대로 탐색
2. 스택이 비었거나 POP과 다르면 PUSH
3. TOP과 같으면 POP -> 짝 제거
4. 마지막에 스택이 비어있으면 '좋은 단어'

[복잡도]
- 시간: o(n * l) -> 각 단어에 대해 한번씩 순회
- 공간: o(l) -> 각 단어마다 최대 스택에 문자 전부 쌓일 수 있음
"""

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    words = input().strip()

    if len(words) % 2 == 1: continue

    for w in words:
        if not stack or stack[-1] != w:
            stack.append(w)
        else:
            stack.pop()
    
    if not stack:
        cnt += 1

print(cnt)