"""
# 아이디어
- for문을 이용하여 각 반복마다 괄호 문자열 입력받기
- 입력된 문자열 s를 앞부터 한글자씩 반복하며
  - 글자가 '('이면 ps에 push
  - 글자가 ')'이고 ps가 비어있지 앟으면 pop, ps가 비어있으면 NO
- 문자열 s의 끝까지 도달했을 때 ps가 비어있으면 YES, 아니면 NO)

# 시간복잡도
- 2 <= s <= 50
- 시간복잡도: O(50 * T)

# 자료구조
- 테스트데이터의 개수를 담는 int형 변수 T
- 각 반복마다 입력을 저장할 str형 변수 s
- 각 문자열마다 괄호를 저장할 str형 배열 ps
- 각 문자열마다 vps 여부를 저장할 bool형 변수 isvps
- vps 여부를 판단한 결과를 저장할 int형 변수 result
"""

import sys
input = sys.stdin.readline
write = sys.stdout.write

def solve():
    T = int(input())
    results = []

    for _ in range(T):
        s = input().strip()
        ps = []
        isvps = True
        
        for ch in s:
            if ch == "(":
                ps.append(ch)
            elif ch == ")":
                if not ps:
                    isvps = False
                    break
                ps.pop()
        
        results.append("YES" if not ps and isvps else "NO")
    
    write("\n".join(results))

if __name__ == "__main__":
    solve()