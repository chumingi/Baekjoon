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
    else:
        results.append(dq[-1] if dq else "-1")
print("\n".join(results))