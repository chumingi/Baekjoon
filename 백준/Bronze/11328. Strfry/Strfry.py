from collections import Counter
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
for i in range(N):
    first, second = input().split()
    write("Possible\n") if Counter(first) == Counter(second) else write("Impossible\n")