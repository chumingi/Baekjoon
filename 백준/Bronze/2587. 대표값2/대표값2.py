# 입력: 다섯 줄에 각각 하나의 자연수
# 출력: 첫 줄에 평균, 둘째 줄에 중앙값

nums = sorted([int(input()) for _ in range(5)])
print(int(sum(nums)/5))
print(nums[2])