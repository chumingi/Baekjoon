"""
# 아이디어
- 백트래킹 재귀함수 내에서 for문에서 1~n 중 하나 선택하여 결과값에 추가
- 재귀함수 호출
- 중복을 방지하기 위해 방문 체크
- 재귀함수 내에서 number가 n일 때 print 후 종료

# 시간복잡도
- 중복이 불가능한 경우 => N! (N <= 10)
- N = 8 <= 10, 가능

# 자료구조
- 방문여부를 확인하는 bool 배열
- 선택한 값들을 저장하는 int 배열
"""

import sys
input = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, input().split())
res = []
chk = [False] * (N+1)

def recur(number):
    if number == M:
        write(' '.join(list(map(str, res))) + "\n")
        return
    
    for i in range(1, N+1):
        if not chk[i]:
            chk[i] = True
            res.append(i)
            recur(number+1)
            chk[i] = False
            res.pop()
recur(0)