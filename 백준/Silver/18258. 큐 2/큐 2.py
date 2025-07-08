from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
results = []

for _ in range(N):
    cmd = input().strip()

    if cmd == "pop":
        results.append(queue.popleft() if queue else "-1")
    elif cmd == "size":
        results.append(str(len(queue)))
    elif cmd == "empty":
        results.append("0" if queue else "1")
    elif cmd == "front":
        results.append(queue[0] if queue else "-1")
    elif cmd == "back":
        results.append(queue[-1] if queue else "-1")
    else:
        _, x = cmd.split()
        queue.append(x)
sys.stdout.write("\n".join(results) + "\n")