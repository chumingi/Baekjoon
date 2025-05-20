A = int(input())
B = int(input())
C = int(input())
abc = str(A * B * C)
ztn = [0] * 10

for c in abc:
    ztn[int(c)] += 1
for i in range(10):
    print(ztn[i])