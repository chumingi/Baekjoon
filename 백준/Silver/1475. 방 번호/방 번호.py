N = int(input())
digit_count = [0] * 10

while N > 0:
    digit_count[N % 10] += 1
    N //= 10

six_and_nine = (digit_count.pop(6) + digit_count.pop(8) + 1) // 2
another_max = max(digit_count)
if (six_and_nine > another_max):
    print(six_and_nine)
else:
    print(another_max)