from collections import Counter

first = input()
second = input()

diff = Counter(first) - Counter(second)
diff += Counter(second) - Counter(first)

print(sum(diff.values()))