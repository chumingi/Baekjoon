from collections import deque
import sys
input = sys.stdin.readline

results = []

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()

    if n == 0:
        ac = deque()
    else:
        ac = deque(arr[1:-1].split(","))

    is_reversed = False
    error_flag = False

    for cmd in p:
        if cmd == "R":
            is_reversed = not is_reversed
        else: # cmd == "D"
            if ac:
                ac.pop() if is_reversed else ac.popleft()
            else:
                error_flag = True
                break
    if error_flag:
        results.append("error")
    else:
        if is_reversed:
            ac.reverse()
        results.append('[' + ','.join(ac) + ']')
print('\n'.join(results))