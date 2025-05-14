# 입력: 다섯 줄에 각각 하나의 자연수
# 출력: 첫 줄에 평균, 둘째 줄에 중앙값

nums = sorted([int(input()) for _ in range(5)])
print(int(sum(nums)/5))
print(nums[2])

# 시간복잡도: O(n log n) - 리스트 정렬에 소요되는 시간
# 공간복잡도: O(n) - 입력된 숫자를 저장하는 리스트의 크기