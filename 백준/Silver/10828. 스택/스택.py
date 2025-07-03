import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
stack = []

for _ in range(N):
    cmd = input().strip()
    
    if cmd.startswith("push"):
        p, x = cmd.split()
        stack.append(x)
    elif cmd == "pop":
        write(stack.pop() + "\n") if stack else write("-1\n")
    elif cmd == "size":
        write(str(len(stack)) + "\n")
    elif cmd == "empty":
        write("1\n") if not stack else write("0\n")
    elif cmd == "top":
        write(stack[-1] + "\n") if stack else write("-1\n")
    else:
        continue