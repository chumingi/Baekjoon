N = input()
digit_count = [0] * 10

for digit in N:
    digit_count[int(digit)] += 1

six_and_nine = (digit_count[6] + digit_count[9] + 1) // 2
digit_count[6] = digit_count[9] = 0
print(max(max(digit_count), six_and_nine))