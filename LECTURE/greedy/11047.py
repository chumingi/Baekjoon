"""
# 아이디어
- 동전을 저장한 뒤 반댈로 뒤집기
- for문을 이ㅛㅇ하여 동전 사용 개수 추가
- 동전 사용한 만큼 k 감소

# 시간복잡도
- 1부터 n까지 for문을 이용해 k 업데이트
- O(n)

# 자료구조
- 동전의 개수를 저장하는 int 변수
- 남은 금액을 저장하는 int 변수
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += k // each_coin
    k %= each_coin
print(cnt)