""" 입력
첫째 줄: 주어지는 명령의 수 N (1 ≤ N ≤ 10,000 입력
둘째 ~ N번째 줄: 명령이 하나씩 입력
명령어: push x, pop, size, empty, top
1 <= 주어지는 정수 <= 100,000"""
""" 출력
출력해야 하는 명령어가 입렭될 때마다 한 줄에 하나씩 출력
출력해야 하는 명령어: pop, top, size, empty"""

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

""" 시간복잡도: O(1) per operation
- 각 명령어는 리스트(stack)의 push/pop/top 등 기본 연산만 수행
- N개의 명령 처리 → O(N)"""
""" 공간복잡도: O(N)
- 스택에 최대 N개의 숫자 저장 가능"""