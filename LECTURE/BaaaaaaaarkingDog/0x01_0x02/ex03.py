"""문제 3
N이 제곱수이면 1을, 아니면 0을 반환하는 함수 func3(int N)을 
작성하라. N은 10억 이하의 자연수이다.

func3(9) = 1
func3(693953651) = 0
func3(756580036) = 1
"""

def func3(N):
    i = 1
    while (i**2 <= N):
        if (i**2 == N):
            print(i)
            return 1
        i += 1
    print(i)
    return 0

print(func3(9))
print(func3(693953651))
print(func3(756580036))