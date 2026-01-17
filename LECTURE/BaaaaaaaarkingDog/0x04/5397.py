""" 입력
첫째 줄: 테스트케이스 개수 입력
테스트케이스 길이(L): 1 <= L <= 1,000,000
'-': 커서 앞에 글자가 존재한다면 제거
'<'와 '>': 왼쪽/오른쪽에 글자가 존재한다면 커서를 1칸 이동"""
""" 출력
각 테스트케이스에 대한 비밃번호 출력"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    left = deque()
    right = deque()
    for pw in input().strip():
        if pw == "-":
            if left:
                left.pop()
        elif pw == "<":
            if left:
                right.appendleft(left.pop())
        elif pw == ">":
            if right:
                left.append(right.popleft())
        else:
            left.append(pw)
    print(''.join(left + right))

""" 시간복잡도: O(T * L)
- T: 테스트케이스 개수
- L: 각 테스트케이스의 최대 길이 (1,000,000)
- 각 문자 처리 및 결과 문자열 조합 모두 O(1) 또는 O(L)"""
""" 공간복잡도: O(T * L)
- 모든 문자열을 저장하기 위한 공간 필요 (최대 약 10^6 * T 문자)"""