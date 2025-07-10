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