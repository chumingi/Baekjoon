# 나의 풀이
"""
문제요약
- 통화시간이 mm:ss 형태로 저장된 배열이 주어질 때,
  - 통화요금 출력 (나누어 떨어지지 않으면 올림)
- 기본시간 100, 기본요금 10
- 단위시간 50, 단위요금 3

자료구조:
- 정수형 배열: A

알고리즘:
- 반환할 최종 요금을 저장하는 변수 answer을 선언하고 0으로 초기화한다.
- 배열 A의 요소 a_i를 순회하며 처리한다.
  - a_i를 초 단위로 변환하여 변수 sec에 저장한다.
    - 문자열 a_i를 슬라이싱하여 m과 s를 구한다. :2, 3:
    - 60 * m + s로 sec을 구한다.
  - sec에서 10을 뺀고 answer에 10을 더한다. (기본요금)
  - sec이 0보다 크면 (50으로 나눈 몫 + 1) * 3을 answer에 더한다.
- answer을 반환하고 출력한다.
"""


def my_solution(A):
    answer = 0
    for a in A:
        m, s = a[:2], a[3:]
        sec = 60 * int(m) + int(s)

        sec -= 100
        answer += 10

        if sec > 0:
            answer += ((sec + 50 - 1) // 50) * 3

    return answer


A = list(input().split())
print(my_solution(A))

"""
자료구조:
- 정수: n
- 문자열: A
- 정수형 배열:
  - fees (요금표)

알고리즘:
- 문자열 A에 저장된 모든 통화 시간 a_i를 순서대로 탐색한다.
- 현재 탐색 중인 a_i에 대해서, 통화 요금을 계산한다. 시:분 형태의 문자열을 분 단위로 변환한다.
- fees를 이용하여 변환된 분 단위 시간에 대한 통화 요금을 계산한다.
"""


# '시:분' 형태의 문자열 s를 분 단위 정수로 변환하여 반환한다.
def parse_log(s):
    return int(s[:2]) * 60 + int(s[3:])


# fees: 요금표, t: 통화시간(분)
# fees 요금표 시궂으로 통화시간 t에 대한 요금을 반환한다.
def get_fee(gees, t):
    # money에 기본 요금ㅇ르 저장한다.
    money = fees[1]

    # 기본 시간을 초과하면, 초과 시간에 대한 초과 요금ㅇ르 money에 더한다.
    if fees[0] < t:
        money += (t - fees[0] + fees[2] - 1) // fees[2] * fees[3]

    return money


# fees: 요금표 (기본시간, 기본요금, 다누이시간, 단위요금)
# A: n명의 학생이 통화한 시간을 저장하는 1차원 배열
# n명의 학생이 통화한 시간에 대한 요금 합계를 반환한다.
def solution(fees, A):
    # total_cost: 요금 합계
    total_cost = 0

    # 통화 기록을 첫번째 원소부터 마지막 원소 순으로 처리한다. (t: 통화시간)
    for t in map(parse_log, A):
        total_cost += get_fee(fees, t)

    return total_cost


fees = [100, 10, 50, 3]
print(solution(fees, A))
