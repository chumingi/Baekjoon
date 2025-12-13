"""
# 아이디어
- n개의 숫자 정렬
- for문을 통해 이진탐색 수행
- 이진탐색에서 데이터 찾으면 1, 없으면 0

# 시간복잡도
- n개 입력값 정렬: n * logn
- n개 중에서 m개를 탐색
- 종합: O((n + m)logn)

# 자료구조
- n개의 숫자를 담는 int 배열
- m개의 숫자를 담는 int 배열
"""

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))
res = []

# 이진탐색 가능하도록 정렬
nums.sort()

# 이진 탐색
"""
def binary_search(low, high, target):
    if low > high or nums[high] < target:
        res.append(0)
        return
    else:
        mid = (low + high) // 2
        if nums[mid] == target:
            res.append(1)
        elif nums[mid] < target:
            binary_search(mid+1, high, target)
        else:
            binary_search(low, mid-1, target)

for t in target_list:
    binary_search(0, n-1, t)
sys.stdout.write("\n".join(list(map(str, res))))
"""

import bisect
for t in target_list:
    i = bisect.bisect_left(nums, t)
    res.append('1' if i < len(nums) and nums[i] == t else '0')
sys.stdout.write("\n".join(list(res)))