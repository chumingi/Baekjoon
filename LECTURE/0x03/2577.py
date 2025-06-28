""" 입력
첫째 ~ 셋째 줄: 100 <= A, B, C <= 1000인 세 자연수 A, B, C 입력"""
""" 출력
첫째 ~ 열째 줄: A * B * C에 포함된 0 ~ 9의 개수를 한 줄에 하나씩 출력"""

A = int(input())
B = int(input())
C = int(input())
product = str(A * B * C)
digit_count = [0] * 10

for digit in product:
    digit_count[int(digit)] += 1
for count in digit_count:
    print(count)

""" 시간복잡도: O(D)
- D: A × B × C의 자릿수 (최대 약 9자리, 100 × 100 × 1000 = 1,000,000 ~ 100,000,000)
- 각 자릿수를 순회하며 10칸짜리 배열을 갱신하는 데 걸리는 시간 → O(D)"""
""" 공간복잡도: O(1)
- 고정된 크기 배열(숫자 0~9의 빈도 수)만 사용 → O(10) = O(1)
- 입력 숫자 A, B, C와 정수형 변수 몇 개 외에는 추가 메모리 없음"""