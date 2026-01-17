"""
[문제 유형] 스택 / 문자열

[핵심 조건]
- 한 문장마다 괄호의 균형 검사
- 한 줄 입력, 마지막 줄은 단독 '.'

[풀이 아이디어]
1. 여는 괄호 → 스택에 push
2. 닫는 괄호 → 스택 top과 매칭되는지 확인
3. 문장 끝에서 스택이 비었으면 "yes", 남았으면 "no"

[예외 케이스]
- 닫는 괄호인데 스택이 비어있음
- 매칭되지 않은 여는 괄호가 남음

[복잡도]
- 시간: O(N)
- 공간: O(N)
"""

import sys
input = sys.stdin.readline

pair = {')':'(', ']':'['}
results = []

while True:
    s = input().rstrip()
    if s == '.': break

    stack = []
    is_balanced = True

    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or pair[ch] != stack[-1]:
                is_balanced = False
                break
            stack.pop()
    results.append("yes" if is_balanced and not stack else "no")
print("\n".join(results))