from collections import Counter
c = Counter

first = input()
second = input()
c1 = c(first) - c(second)
c2 = c(second) - c(first)
print(c1.total() + c2.total())