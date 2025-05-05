import sys
input = sys.stdin.readline
write = sys.stdout.write

N, x = map(int, input().split())
arr = map(int, input().split())

for num in arr:
    if num < x:
        write(f"{num} ")