nums = [int(input()) for _ in range(7)]
odds = [n for n in nums if n % 2 == 1]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)

# 시간복잡도: O(n) - 입력된 7개의 숫자를 한 번씩 순회하여 홀수를 추출하고, 합과 최소값을 계산
# 공간복잡도: O(n) - 홀수들을 저장하는 리스트 odds가 최대 n개의 요소를 가질 수 있음