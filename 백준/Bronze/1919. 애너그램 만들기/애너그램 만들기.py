a = input()
b = input()
freq = [0] * 26

for ch in a:
    freq[ord(ch) - ord('a')] += 1
for ch in b:
    freq[ord(ch) - ord('a')] -= 1

print(sum(abs(x) for x in freq))