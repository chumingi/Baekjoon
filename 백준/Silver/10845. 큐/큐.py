from collections import deque
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().strip()

    if cmd == "pop":
        write(queue.popleft() + "\n") if queue else write("-1\n")
    elif cmd == "size":
        write(str(len(queue)) + "\n")
    elif cmd == "empty":
        write("1\n") if not queue else write("0\n")
    elif cmd == "front":
        write(queue[0] + "\n") if queue else write("-1\n")
    elif cmd == "back":
        write(queue[-1] + "\n") if queue else write("-1\n")
    else:
        _, X = cmd.split()
        queue.append(X)