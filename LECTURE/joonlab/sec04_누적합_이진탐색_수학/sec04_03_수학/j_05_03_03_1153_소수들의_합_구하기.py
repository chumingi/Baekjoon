"""
자료구조:
- 정수형 배열: A

알고리즘:
- 배열 A에 저장된 모든 원소 a_i를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 a_i중에서 소수인 a_i의 합을 출력한다.
- 2에서 루트 a_i 중에서 a_i를 나누어서 나머지가 0인 수 (약수)가 있으면 소수가 아니고, 없으면 소수이다.
"""


# A: 여러 개의 수를 저장한 1차원 배열
# 배열 A에 포함된 소수의 합을 반환한다.
def solution(A):
    # 배열 A에 포함된 수를 순서대로 탐색한다.
    # answer: 배열 A에 포함된 소수의 합을 저장한다.
    answer = 0
    for a in A:
        if is_prime(a):
            answer += a

    return answer


# a가 소수이면 True, 아니면 False를 반환한다.
# 루트 a 시간복잡도로 소수를 구한다.
def is_prime(a):
    # 1은 소수가 아니다.
    if a < 2:
        return False

    # 2 ~ 루트 a 사이에 a의 약수가 있으면 a는 소수가 아니다.
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1

    # 2 ~ 루트 a 사이에 a의 약수가 없으면 a는 소수다.
    return True


A = list(map(int, input().split()))
print(solution(A))

# 추가 문제: 백준 1978, 1929, 2581
