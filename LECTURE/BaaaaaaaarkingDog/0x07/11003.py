"""
[문제 유형]
- 슬라이딩 윈도우 + 최솟값 유지 → Monotonic Queue

[문제 요약]
- 각 i에 대해 A[i-L+1] ~ A[i] 중 최소값 출력
- i-L+1 < 0 이면 범위 제외

[입력 조건]
- N ≤ 5 * 10^6 → O(N log N)도 TLE → O(N) 필요
- L ≤ N

[출력 조건]
- 각 i에 대한 D_i 출력 (공백 구분)

[제약 분석 및 시간복잡도 판단]
- min() 사용 시 O(NL) → TLE
- 각 수는 deque에 한 번 들어가고 한 번 나가야 함 → O(N)

[자료구조 / 알고리즘 전략]
- deque에 (값, 인덱스) 저장
- 새 값 A[i] 삽입 전: 뒤에서 자신보다 큰 값 제거
- 앞에서 윈도우 범위 밖 인덱스 제거
- 앞에 있는 값이 현재 구간의 최솟값

[예외 / 실수 방지 포인트]
- 윈도우 벗어난 값 처리 조건 정확히
- sys.stdin.readline 사용해 빠르게 입력
"""

from collections import deque
import sys
input = sys.stdin.readline
write = sys.stdout.write

N, L = map(int, input().split())
A = list(map(int, input().split()))
dq = deque()

for i in range(N):
    while dq and dq[-1][0] > A[i]:
        dq.pop()
    dq.append((A[i], i))
    if i - dq[0][1] >= L:
        dq.popleft()
    write(str(dq[0][0]) + "\n")

"""
[시간복잡도] O(N)
- 각 수는 deque에 최대 1번 push, 1번 pop
- 전체 처리 = 2N번 연산

[공간복잡도] O(N)
- 입력 배열 A = O(N)
- deque 내부 = 최대 O(L)
"""