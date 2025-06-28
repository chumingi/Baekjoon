""" 입력
첫째 줄: 1,000,000보다 작은 자연수 N 입력"""
""" 출력
첫째 줄: 필요한 세트의 개수 출력"""

N = input()
digit_count = [0] * 10

for digit in N:
    digit_count[int(digit)] += 1

six_and_nine = (digit_count[6] + digit_count[9] + 1) // 2
digit_count[6] = digit_count[9] = 0
print(max(max(digit_count), six_and_nine))

""" 시간복잡도: O(D)
- D: 입력 숫자 N의 길이 (자릿수)
- 각 자릿수를 1번씩 순회 → O(D)
- 0~9까지 중 최대값 계산 → O(10) = O(1)"""
""" 공간복잡도: O(1)
- 고정 크기 배열 count[10]만 사용
- 추가적인 메모리 없음"""