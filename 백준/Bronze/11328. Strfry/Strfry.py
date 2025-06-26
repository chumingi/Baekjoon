import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
for i in range(N):
    first, second = input().split()
    write("Possible\n") if sorted(first) == sorted(second) else write("Impossible\n")