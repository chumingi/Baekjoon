"""
도(A): 0 1 1 1
개(B): 0 0 1 1
걸(C): 0 0 0 1
윷(D): 0 0 0 0
모(E): 1 1 1 1
"""

for _ in range(3):
    count = list(map(int, input().split())).count(0)
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    else:
        print("D")

# 시간 복잡도: O(1) - 입력 크기가 고정되어 있으며, 각 줄마다 고정된 수의 연산을 수행하므로 시간 복잡도는 상수 시간
# 공간 복잡도: O(1) - 추가적인 데이터 구조를 사용하지 않으며, 고정된 수의 변수만 사용하므로 공간 복잡도도 상수 공간