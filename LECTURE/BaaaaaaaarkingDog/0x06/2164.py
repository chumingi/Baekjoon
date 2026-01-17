""" 입력
첫째 줄: 정수 N (1 <= N <= 500,000) 입력"""
""" 출력
첫째 줄: 남게 되는 카드의 번호 출력"""

from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])

for _ in range(N-1):
    cards.popleft()
    # cards.rotate(-1)
    cards.append(cards.popleft())
print(cards[0])

""" 시간복잡도: O(N)
- deque의 popleft(), append()는 O(1)
- 총 연산 횟수는 N-1회 → O(N)"""
""" 공간복잡도: O(N)
- 카드 N장을 저장할 deque 필요 → O(N)"""