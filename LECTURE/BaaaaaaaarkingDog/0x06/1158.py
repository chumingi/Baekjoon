""" 입력
첫째 줄: N과 K가 공백을 기준으로 구분되어 입력 (1 <= K <= N <= 5,000)"""
""" 출력
첫째 줄: 요세푸스 수열이 쉼표로 구분되어 출력"""

from collections import deque

N, K = map(int, input().split())
queue = deque([i+1 for i in range(N)])
results = []

for _ in range(N-1):
    queue.rotate(-K+1)
    results.append(queue.popleft())
results.append(queue[0])
print("<" + ", ".join(map(str, results)) + ">")

""" 시간복잡도: O(N)
- queue.rotate(k): O(1) 수준
- popleft(): O(1)
- N번 반복 → 총 O(N)"""
""" 공간복잡도: O(N)
- queue에는 최대 N개 요소
- results 리스트도 N개 저장"""