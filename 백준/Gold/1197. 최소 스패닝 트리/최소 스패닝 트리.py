"""
# 아이디어
- 간선을 인접리스트 형태로 저장
- 시작점을 힙에 저장
- 힙이 빌 때까지,
- 방문하지 않은 인접한 노드를 방문 체크, 비용 추가, 연결된 간선을 힙에 추가

# 시간복잡도
- O(e * loge) - e: 간선 수

# 자료구조
- 간선 정보저장하는 인접리스트 (가중치, 노드 쌍)
- 힙
- 방문 여부를 저장하는 boolean 배열
- mst 결과갑승ㄹ 저장하는 int
"""

import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
result = 0

for i in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

heap = [(0, 1)]  # 1: 시작점 노드, 0: 가중치
while heap:
    w, v = heapq.heappop(heap)
    if visited[v]:
        continue
    
    visited[v] = True
    result += w
    for nw, nv in edges[v]:
        if not visited[nv]:
            heapq.heappush(heap, (nw, nv))
print(result)