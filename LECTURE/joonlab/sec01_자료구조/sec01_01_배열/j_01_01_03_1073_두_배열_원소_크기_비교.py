"""
자료구조:
- 정수: a, b
- 정수형 배열: A, B
알고리즘:
- 배열 a, B의 모든 원소 a_i, b_i를 순서대로 탐색한다.
a_i > b_i인 원소의 수를 a, a_i < b_i인 원소의 수를 b에 저장한다.
a > b이면 1을 출력하고, a <= b이면 0을 출력한다.
"""


# A, B: 각각 n개의 정수가 저장된 1차원 배열
# a > b이면 1, 그렇지 않으면 0을 반환한다.
def solution(A, B):
    a, b = 0, 0
    for x, y in zip(A, B):
        if x > y:
            a += 1
        elif x <= y:
            b += 1
    return int(a > b)


# 입력을 받는다.
A = map(int, input().split())
B = map(int, input().split())
print(solution(A, B))

# 추가 문제: 백준 4101, 1330
