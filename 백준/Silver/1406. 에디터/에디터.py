import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
M = int(input())


for _ in range(M):
    cmd = input().strip()
    if cmd == "L":
        if left:
            right.append(left.pop())
    elif cmd == "D":
        if right:
            left.append(right.pop())
    elif cmd == "B":
        if left:
            left.pop()
    else:
        P, S = cmd.split()
        left.append(S)
print(''.join(left + right[::-1]))