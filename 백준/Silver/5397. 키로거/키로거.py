from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    left = deque()
    right = deque()
    for pw in input().strip():
        if pw == "-":
            if left:
                left.pop()
        elif pw == "<":
            if left:
                right.appendleft(left.pop())
        elif pw == ">":
            if right:
                left.append(right.popleft())
        else:
            left.append(pw)
    print(''.join(left + right))