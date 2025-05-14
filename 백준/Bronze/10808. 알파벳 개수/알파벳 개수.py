S = input().strip()
alphabets = [0] * 26

for c in S:
    alphabets[ord(c) - ord('a')] += 1
print(*alphabets)