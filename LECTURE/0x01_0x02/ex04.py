"""문제 4
N 이하 수 중에서 가장 큰 2의 거듭제곱수를 반환하는 함수
func4(int N)을 작성하라. N은 10억 이하의 자연수이다.

func4(5) = 4
func4(97616282) = 67108864
func4(1024) = 1024
"""

import math
def func4(N):
    val = 1
    while (2*val <= N): val *= 2
    return val

    # 다른 방법
    power = int(math.log2(N))
    return 2**power

print(func4(5))
print(func4(97616282))
print(func4(1024))
print("시간복잡도: O(2**N)")