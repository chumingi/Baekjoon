from collections import deque
import sys
write = sys.stdout.write

n = int(input())
moves = list(map(int, input().split()))
balloons = deque((i + 1, m) for i, m in enumerate(moves))

while balloons:
    idx, move = balloons.popleft()
    write(f"{idx} ")

    if not balloons:
        break

    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)