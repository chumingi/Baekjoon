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
    write(' '.join(map(str, range(A + 1, B))))