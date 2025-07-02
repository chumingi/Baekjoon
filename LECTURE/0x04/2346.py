""" 입력
첫째 줄: 자연수 N(1 <= N <= 1,000) 입력
둘째 줄: 풍선 안에 적힌 0이 아닌 수들이 공백으로 구분되어 입력"""
""" 출력
터진 풍선의 번호를 순서대로 나열하여 출력"""

from collections import deque
import sys
write = sys.stdout.write

n = int(input())
moves = list(map(int, input().split()))
balloons = deque((i + 1, m) for i, m in enumerate(moves))

while balloons:
    idx, move = balloons.popleft()
    write(f"{idx} ")

    if not balloons:
        break

    # 회전 방향에 따라 처리
    if move > 0:
        balloons.rotate(-(move - 1))  # 현재 꺼낸 것 제외
    else:
        balloons.rotate(-move)

""" 시간복잡도: O(N)
- 각 풍선을 정확히 한 번만 터뜨림 (popleft: O(1), rotate: O(k), k ≤ N)
- deque의 rotate 연산도 내부적으로 O(k), Python은 C로 최적화되어 있어 빠름"""
""" 공간복잡도: O(N)
- 풍선 정보를 deque에 저장하므로 N개의 쌍 필요"""