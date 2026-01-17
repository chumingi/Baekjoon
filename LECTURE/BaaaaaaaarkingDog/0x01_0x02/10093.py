# 입력: 첫 줄에 두 정수 A, B (1 <= A, B <= 10^15, A-B <= 100,000) 입력
# 출력: 첫째 줄에는 A와 B 사이의 정수의 개수, 둘째 줄에는 A와 B 사이의 모든 양수 오름차순 출력

import sys
input = sys.stdin.readline
write = sys.stdout.write

A, B = map(int, input().split())
if A > B:
    A, B = B, A
if (B-A == 0 or B-A == 1):
    write("0")
else:
    count = B - A - 1
    write(f"{count}\n")
    for i in range(A + 1, B):
        write(f"{i} ")
