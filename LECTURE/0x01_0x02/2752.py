"""방법 1 - 기본 정렬 사용
a = sorted(map(int, input().split()))
print(*a)
"""
# 시간복잡도: O(nlogn) - sorted() 함수는 Timsort 알고리즘을 사용하며, 평균 및 최악의 경우 시간 복잡도는 O(n log n)
# 공간 복잡도: O(n) - sorted()는 새로운 리스트를 생성하므로 입력 크기 n에 비례하는 추가 메모리를 사용

"""방법 2 - 리스트의 sort() 메소드 사용
a = list(map(int, input().split()))
a.sort()
print(*a)
"""
# 시간 복잡도: O(nlogn) - sort() 메서드도 Timsort를 사용하기 때문
# 공간 복잡도: O(1) - 리스트를 제자리에서 정렬하므로 추가 메모리 사용이 거의 없음

# 방법 3 - 조건문을 이용한 수동 정렬
a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)
# 시간 복잡도: O(1) - 고정된 수의 비교 및 교환만 수행하므로 입력 크기에 관계없이 일정한 시간에 실행
# 공간 복잡도: O(1) - 추가적인 데이터 구조를 사용하지 않으므로 메모리 사용이 최소화

"""방법 4 - min()과 max() 메소드 사용
nums = list(map(int, input().split()))
min_val = min(nums)
max_val = max(nums)
mid_val = sum(nums) - min_val - max_val
print(min_val, mid_val, max_val)
"""
# 시간 복잡도: O(n) - min(), max(), sum() 함수는 각각 리스트를 한 번씩 순회하므로 전체 시간 복잡도는 O(n)
# 공간 복잡도: O(1) - 입력값을 리스트로 저장하므로 입력 크기 n에 비례하는 메모리를 사용