"""
자료구조:
- 정수: n
- 문자열 배열: A
- 정수형 배열:
  - T: 유형 1의 질의 결과를 초 단위로 저장

알고리즘:
- 배열 A에 있는 모든 질의 a_i를 순서대로 탐색하면서 질의 a_i를 처리한다.
- 질의 a_i가 유형 1이면,
  - 시간 구간 h1:m1:s1 ~ h2:m2:s2의 값을 1만큼 증가시킨다.
  - h1:m1:s1, h2:m2:s2를 각각 초 단위 i, j로 환산하여 배열 T의 T[i]부터 T[j-1]까지의 값을 1만큼 증가시킨다.
  - 누적합 개념을 이용하여 T[i]를 1만큼 증가시키고 T[j]를 1만큼 감소시켜서 O(1)에 빠르게 처리한다.
- 질의 a_i가 유형 2이면,
  - h1:m1:s1 ~ h2:m2:s2의 값을 출력한다.
  - h1:m1:s1, h2:m2:s2를 각각 초 단위 i, j로 환산하여 배열 T의 T[i]부터 T[j-1]까지의 값의 합을 출력한다.
  - 누적합 개념을 이용하여 T[0]부터 순서대로 배열 T의 값을 누적하여 더한다. 그 후에 T[i]부터 T[j-1]까지의 값을 모두 더해서 출력한다.
"""


# n, A: n개의 질의 (질의 유형: 1, 2)가 저장된 배열 A
# 유형 2의 질의 결과를 반환한다.
def solution(n, A):
    # n개의 질의를 첫번째 질의부터 n번째 질의까지 순서대로 처리한다.
    # T: 전체 시간 구간 00:00:00에서 23:59:59 값을 저장한다. (초깃값: 0)
    # T[i]는 시간 구간 i ~ (i+1) 초 구간의 값을 저장한다.
    # 24시간 = 24 * 60 * 60 = 86,400초이므로 배열 T의 크기는 86,400이다.
    T = [0] * 24 * 60 * 60
    answer = 0
    for a in A:
        if a[0] == "1":
            add_query(T, translate_time(a[1]), translate_time(a[2]))
        else:
            answer = get_sum(T, translate_time(a[1]), translate_time(a[2]))

    return answer


# hh:mm:ss 형식의 문자열로 되어 있는 시간을 초 단위의 정수로 반환한다.
def translate_time(t):
    # 1시간 = 60 * 60 = 3,600초, 1분 = 60초
    return int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:])


# i부터 j-1까지의 배열 T의 원소에 1을 더한다.
# T[i]에 1을 더하고, T[j]에 1을 빼는 누적합을 이용하여 O(1)에 해결한다.
def add_query(T, i, j):
    T[i] += 1
    T[j] -= 1


# i부터 j-1까지의 배열 T의 원소의 합을 반환한다.
def get_sum(T, i, j):
    # 누적합을 이용하여 배열 T를 완성한다.
    for t in range(1, 24 * 60 * 60):
        T[t] += T[t - 1]

    # T[i] ~ T[j-1]까지의 합을 ret에 저장하고 반환한다.
    # 아래 코드를 return sum(t[i:j])로 대체할 수 있다.
    ret = 0
    for t in range(i, j):
        ret += T[t]
    return ret


n = int(input())
A = [list(input().split()) for _ in range(n)]
print(solution(n, A))
