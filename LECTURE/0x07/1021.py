"""
[문제 유형]
- 시뮬레이션 + 덱 + 최소 연산 판단

[문제 요약]
- 1부터 N까지의 수가 들어있는 큐
- 특정 수들을 순서대로 꺼내기 위해 최소 회전 연산 횟수를 구하라
- 가능한 연산: 
  1) 왼쪽 회전 (rotate -1), 
  2) 오른쪽 회전 (rotate +1), 
  3) 맨 앞 제거

[입력 조건]
- N (큐 크기) ≤ 50
- 뽑을 수의 개수 M ≤ N
- 총 연산량이 작아서 O(N^2)도 가능하지만 O(N) 구현이 바람직

[출력 조건]
- 회전 연산 횟수의 총합 출력

[제약 분석 및 시간복잡도 판단]
- rotate 연산은 deque에서 O(1)
- index(), popleft(), append도 모두 O(1)
- 총 M번 대상 뽑기 → O(M × N) 가능

[자료구조 / 알고리즘 전략]
- deque 사용: 회전 및 pop 양방향 처리
- 현재 뽑을 수의 위치를 index로 파악
  → index ≤ len(dq)//2 → 왼쪽 회전
  → index > len(dq)//2 → 오른쪽 회전
- 뽑은 후 항상 popleft()

[예외 / 실수 방지 포인트]
- rotate 방향과 횟수 계산 시 조건 정확히
- 결과 누적은 회전 연산만 포함해야 함 (popleft는 제외)
"""

from collections import deque

N, M = map(int, input().split())
dq = deque(range(1, N+1))
targets = list(map(int, input().split()))
target_idx = 0
turns = 0

for i in range(M):
    target_idx = dq.index(targets[i])
    gap = len(dq) - target_idx

    if target_idx <= gap:
        dq.rotate(-target_idx)
        turns += target_idx
    else: # target_idx > gap
        dq.rotate(gap)
        turns += gap
    dq.popleft()
print(turns)

"""
[시간복잡도] O(N × M)
- dq.index(x): O(N) → M개의 타겟마다 수행 → O(N × M) (최악 O(5,000 × 5,000))
- rotate, popleft는 deque에서 O(1)

[공간복잡도] O(N + M)
- deque에 최대 N개 저장
- targets 리스트에 M개 저장
"""