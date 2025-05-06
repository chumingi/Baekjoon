nums = []
for _ in range(7):
    num = int(input())
    if (num%2 == 1):
        nums.append(num)
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))