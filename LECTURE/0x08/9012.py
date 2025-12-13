"""
[문제 유형]  
-> 문자열 / 스택 / 괄호 유효성 검사 (전형적인 자료구조 문제)

[핵심 조건]  
- T ≤ 50 (테스트 케이스 수 적음)
- 괄호 문자열 길이는 최대 50 -> 매우 짧음 -> 시간복잡도 거의 무제한
- 괄호만 주어짐 -> '(', ')' 로만 구성된 문자열

[풀이 아이디어]  
1. 여는 괄호 '('는 스택에 push
2. 닫는 괄호 ')'는 스택 top이 '('일 경우에만 pop
3. 중간에 매칭 안 되거나 마지막에 스택이 남아 있으면 NO
4. 모두 짝 맞고 스택이 비어 있으면 YES

[예외 케이스]  
- 시작부터 ')' -> NO
- 끝났는데 스택에 '(' 남음 -> NO
- "()()" -> YES
- "(()" -> NO

[복잡도]  
- 시간: O(T * L) -> T=50, L=50 -> 총 2,500회 이하
- 공간: O(L) -> 스택 사용
"""

import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())
vps = []

for _ in range(T):
    is_vps = True
    stack = []
    ps = input().strip()

    for ch in ps:
        if ch == "(":
            stack.append(ch)
        else: # ch == ")"
            if not stack or stack[-1] != "(":
                is_vps = False
                break
            stack.pop()
    
    vps.append("YES" if not stack and is_vps else "NO")

write("\n".join(vps))