import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
for i in range(N):
    for j in range(i+1):
        write("*")
    write("\n")