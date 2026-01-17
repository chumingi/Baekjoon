"""
[문제 유형]
- 덱(deque) 구현 시뮬레이션

[문제 요약]
- push_front, push_back: 정수 추가
- pop_front, pop_back: 정수 제거 및 출력
- size, empty: 현재 상태 출력
- front, back: 앞/뒤 값 출력

[입력 조건]
- 명령 개수 N ≤ 10,000
- 입력 크기 작음 → O(1) 연산만 쓰면 충분히 통과

[출력 조건]
- 출력 요구 명령마다 한 줄씩 출력 (명확하게 조건별 처리 필요)

[제약 분석 및 시간복잡도 판단]
- deque 연산: 모든 명령 O(1)
- 총 명령 수 ≤ 10,000 → 시간/메모리 충분

[자료구조 / 알고리즘 전략]
- collections.deque 사용
- 명령어 입력은 sys.stdin.readline으로 빠르게 처리
- 출력은 list에 저장 후 join으로 한 번에 처리 (I/O 최적화)

[예외 / 실수 방지 포인트]
- 빈 덱에서 pop, front, back → -1 출력
- 명령어가 문자열로 들어오므로 정확한 비교 필요
- push 명령은 split()으로 값 분리
"""

from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
results = []

N = int(input())
for _ in range(N):
    cmd = input().strip()

    if cmd.startswith("push_f"):
        p, x = cmd.split()
        dq.appendleft(x)
    elif cmd.startswith("push_b"):
        p, x = cmd.split()
        dq.append(x)
    elif cmd == "pop_front":
        results.append(dq.popleft() if dq else "-1")
    elif cmd == "pop_back":
        results.append(dq.pop() if dq else "-1")
    elif cmd == "size":
        results.append(str(len(dq)))
    elif cmd == "empty":
        results.append("0" if dq else "1")
    elif cmd == "front":
        results.append(dq[0] if dq else "-1")
    else: # cmd == "back"
        results.append(dq[-1] if dq else "-1")
print("\n".join(results))

"""
[시간복잡도] O(N)
- N: 명령의 수 (최대 10,000)
- 각 연산 (append, pop, index, len 등) → O(1)
- 총 N회 수행 → O(N)

[공간복잡도] O(N)
- 덱: 최대 N개 정수 저장 → O(N)
- results 리스트: 출력 최대 N개 → O(N)
"""