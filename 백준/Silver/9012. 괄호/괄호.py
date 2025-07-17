import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())
vps = []

for _ in range(T):
    is_vps = True
    stack = []
    ps = input().strip()

    for ch in ps:
        if ch == "(":
            stack.append(ch)
        else: # ch == ")"
            if not stack or stack[-1] != "(":
                is_vps = False
                break
            stack.pop()
    
    vps.append("YES" if not stack and is_vps else "NO")

write("\n".join(vps))