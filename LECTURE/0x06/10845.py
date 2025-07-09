""" 입력
첫째 줄: 명령의 수 N (1 <= N <= 10,000) 입력
N개의 줄: 명령이 하나씩 입력
push X: 정수 X를 큐에 넣는 연산
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력하는 명령어. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
size: 큐에 들어있는 정수의 개수를 출력하는 명령어
empty: 큐가 비어있으면 1, 아니면 0을 출력하는 명령어
front: 큐의 가장 앞에 있는 정수를 출력하는 명령어. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
back: 큐의 가장 뒤에 있는 정수를 출력하는 명령어. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력"""
""" 출력
출력해야 하는 명령어가 주어질 때마다 하나씩 출력"""

from collections import deque
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().strip()

    if cmd == "pop":
        write(queue.popleft() + "\n") if queue else write("-1\n")
    elif cmd == "size":
        write(str(len(queue)) + "\n")
    elif cmd == "empty":
        write("1\n") if not queue else write("0\n")
    elif cmd == "front":
        write(queue[0] + "\n") if queue else write("-1\n")
    elif cmd == "back":
        write(queue[-1] + "\n") if queue else write("-1\n")
    else:
        _, X = cmd.split()
        queue.append(X)

""" 시간복잡도: O(N)
- N: 명령어의 수 (최대 10,000)
- 각 명령어는 deque의 메서드로 처리됨:
    - append, popleft, len, indexing (front/back) 모두 O(1)"""
""" 공간복잡도: O(N)
- 큐에는 최대 N개의 정수가 들어올 수 있음
- 입력 저장은 따로 하지 않고 실시간 처리함"""