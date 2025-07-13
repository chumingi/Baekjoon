"""
[문제 유형]
- 시뮬레이션 + 문자열 명령어 처리 + deque 사용

[문제 요약]
- 'R': 배열 뒤집기, 'D': 앞에서 제거
- 빈 배열에서 D 수행 시 error 출력
- 명령어 p를 배열에 순서대로 적용한 결과 출력

[입력 조건]
- T ≤ 100
- 명령어 길이 ≤ 10^5
- 배열 길이 ≤ 10^5
- 최대 총 연산 10^7 → O(N) 수준으로 구현해야 함

[출력 조건]
- 배열을 리스트 형식으로 출력하거나 error

[제약 분석 및 시간복잡도 판단]
- 매번 reverse()는 O(N) → TLE 위험
- D가 빈 deque에서 실행되면 error 발생

[자료구조 / 알고리즘 전략]
- deque 사용 (양쪽 pop O(1))
- R 명령은 실제 reverse() 대신 is_reversed 플래그 사용
- 마지막 출력 시 방향에 따라 출력 조정

[예외 / 실수 방지 포인트]
- 빈 배열 입력: split()하면 [''] → deque([]) 처리
- join 사용해 빠른 출력 처리
"""

from collections import deque
import sys
input = sys.stdin.readline

results = []

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()

    if n == 0:
        ac = deque()
    else:
        ac = deque(arr[1:-1].split(","))

    is_reversed = False
    error_flag = False

    for cmd in p:
        if cmd == "R":
            is_reversed = not is_reversed
        else: # cmd == "D"
            if ac:
                ac.pop() if is_reversed else ac.popleft()
            else:
                error_flag = True
                break
    if error_flag:
        results.append("error")
    else:
        if is_reversed:
            ac.reverse()
        results.append('[' + ','.join(ac) + ']')
print('\n'.join(results))

"""
[시간복잡도] O(T * N)
- R 명령은 O(1) (플래그 토글 방식)
- D 명령은 O(1)
- reverse()는 최종 1회만 O(N) (필요 시)
- 총 문자열 처리/출력도 O(N)

[공간복잡도] O(N)
- deque 사용: 최대 100,000개 정수 저장
- 출력 결과 저장: 최대 O(N)
"""