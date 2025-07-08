from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])

for _ in range(N-1):
    cards.popleft()
    cards.rotate(-1)
print(cards[0])