"""
# 아이디어
- 점화식: a_n = a_(n-1) + a_(n-2)
- for문을 이용하여 3부터 n까지의 값을 계싼하고 10007로 나누어 저장

# 시간복잡도
- O(n)

# 자료구조
- 경우의 수 int 배열

"""

import sys
input = sys.stdin.readline

N = int(input())
result = [0, 1, 2]

for i in range(3, N+1):
    result.append((result[i-1] + result[i-2]) % 10007)
print(result[N])