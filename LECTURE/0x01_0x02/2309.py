# 입력: 아홉 줄에 각각 100 이하의 자연수 입력
# 출력: 합이 100이 되는 7개 값을 오름차순으로 한 줄에 한개씩 출력

"""방법 1
heights = [int(input()) for _ in range(9)]
total = sum(heights)
found = False

for i in range(8):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            excluded = {heights[i], heights[j]}
            result = [h for h in heights if h not in excluded]
            result.sort()
            for h in result:
                print(h)
            found = True
            break
    if found:
        break
"""

# 방법 2 - 조합 이용
from itertools import combinations

heights = [int(input()) for _ in range(9)]

for combo in combinations(heights, 7):
    if sum(combo) == 100:
        for h in sorted(combo):
            print(h)
        break

# 시간복잡도: O(nCr) - 9C7 = 36개의 조합을 확인
# 공간복잡도: O(1) - 추가적인 공간을 거의 사용하지 않음

"""방법 3 - 재귀 이용
heights = [int(input()) for _ in range(9)]
selected = []

def dfs(start):
    if len(selected) == 7:
        if sum(selected) == 100:
            for h in sorted(selected):
                print(h)
            exit()
        return
    for i in range(start, 9):
        selected.append(heights[i])
        dfs(i + 1)
        selected.pop()

dfs(0)
"""