"""
문제1: N 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을
반환하는 함수 func1을 작성하라. N은 10만 이하의 자연수이다.

func1(16) = 60
func1(34567) = 278812814
func(27639) = 178254968
"""

def func1(N):
    cnt = 0
    for i in range(1, N+1):
        if (i%3 == 0 or i%5 == 0):
            cnt += i
    return cnt

print(func1(16))
print(func1(34567))
print(func1(27639))