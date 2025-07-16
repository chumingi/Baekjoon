import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    words = input().strip()

    for w in words:
        if not stack or stack[-1] != w:
            stack.append(w)
        else:
            stack.pop()
    if not stack:
        cnt += 1
print(cnt)