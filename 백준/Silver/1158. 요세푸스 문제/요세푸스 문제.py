from collections import deque

N, K = map(int, input().split())
queue = deque([i+1 for i in range(N)])
results = []

for _ in range(N-1):
    queue.rotate(-K+1)
    results.append(queue.popleft())
results.append(queue[0])
print("<" + ", ".join(map(str, results)) + ">")