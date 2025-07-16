import sys
input = sys.stdin.readline

pair = {')':'(', ']':'['}
results = []

while True:
    s = input().rstrip()
    if s == '.': break

    stack = []
    is_balanced = True

    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or pair[ch] != stack[-1]:
                is_balanced = False
                break
            stack.pop()
    results.append("yes" if is_balanced and not stack else "no")
print("\n".join(results))