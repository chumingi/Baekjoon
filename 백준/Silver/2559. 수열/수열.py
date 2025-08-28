"""
# 아이디어
- 투포인터 활용
- 처음 k개 인덱스 저장
- for문을 통해 이전 인덱스 제거, 다음 인덱스 추가, 최고값 갱신

# 시간복잡도
- O(n), n <= 100,000 가능

# 자료구조
- 각 숫자들을 저장하는 int 배열
- k개의 값을 저장하는 int 배열
- 최댓값을 저장하는 int 변수
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
each = 0

for i in range(k):
    each += nums[i]
maxv = each

# 다음 인덱스 넣고 이전 인덱스 빼기
for j in range(k, n):
    each += nums[j]
    each -= nums[j-k]
    maxv = max(maxv, each)

print(maxv)