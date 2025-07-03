import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
current = 1

for _ in range(N):
    num = int(input())

    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        current = 0
        break
print("\n".join(result)) if current else print("NO")