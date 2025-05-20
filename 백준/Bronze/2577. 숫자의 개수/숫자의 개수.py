A = int(input())
B = int(input())
C = int(input())
product = str(A * B * C)
digit_count = [0] * 10

for digit in product:
    digit_count[int(digit)] += 1
for count in digit_count:
    print(count)