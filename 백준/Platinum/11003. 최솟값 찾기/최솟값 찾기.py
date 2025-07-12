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