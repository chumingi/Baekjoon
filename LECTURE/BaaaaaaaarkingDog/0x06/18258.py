""" 입력
첫째 줄: 명령의 수 N (1 <= N <= 2,000,000) 입력
N개의 줄: 명령이 하나씩 입력
주어지는 정수: 1 이상 100,000 이하
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

N = int(input())
queue = deque()
results = []

for _ in range(N):
    cmd = input().strip()

    if cmd == "pop":
        results.append(queue.popleft() if queue else "-1")
    elif cmd == "size":
        results.append(str(len(queue)))
    elif cmd == "empty":
        results.append("0" if queue else "1")
    elif cmd == "front":
        results.append(queue[0] if queue else "-1")
    elif cmd == "back":
        results.append(queue[-1] if queue else "-1")
    else:
        _, x = cmd.split()
        queue.append(x)
sys.stdout.write("\n".join(results) + "\n")

""" 시간복잡도: O(N)
- 각 명령은 deque의 O(1) 연산으로 처리 (append, popleft, indexing)
- 출력도 join을 통해 O(N) 처리
- 총 N개의 명령을 한 번씩만 처리하므로 O(N)"""
""" 공간복잡도: O(N)
- 큐에 들어가는 요소는 최대 N개
- 출력 결과를 저장하는 리스트도 최대 N개"""