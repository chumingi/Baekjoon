"""
'N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로'
'신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사'
'가장 먼저 만나는 단 하나의 탑에서만 수신이 가능'

첫째 줄 입력: 탑의 개수 N (1 <= N <= 5*10^5)
둘째 줄 입력: 탑들의 높이가 공백으로 구분 (1 <= 각 높이 <= 10^8)
첫째 줄 출력: 주어진 탑들의 순서대로 레이저 신호를 수신한 탑들의 번호를 공백 구분하여 출력, 없으면 0 출력
"""

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    towers = list(map(int, input().split()))

    stack = []  # (index, height)
    results = []

    for i, t in enumerate(towers):
        while stack and stack[-1][1] < t:
            stack.pop()
        results.append(0 if not stack else stack[-1][0] + 1)
        stack.append((i, t))
    print(*results)

if __name__ == "__main__":
    solve()