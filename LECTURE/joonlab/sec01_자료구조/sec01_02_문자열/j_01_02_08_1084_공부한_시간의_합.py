"""
자료구조:
- 정수:
- 문자열: A
알고리즘:
- 문자열 A에 저장된 모든 시간 t를 첫번째 시간부터 마지막 시간까지 순서대로 탐색한다.
- 현재 탐색 중인 t의 모든 합을 구한다.
- t를 분 단위로 환산하여 시간 합을 분 단위로 구한다.
- 분 단위로 구한 시간 합을 시:분 형태로 변환한다.
"""


# '시:분' 형태의 문자열 s를 분 단위 정수로 변환하여 반환한다.
def parse_log(s):
    return int(s[0:2]) * 60 + int(s[3:5])


# A: n일 동안 공부한 시간 목록을 저장한 1차원 배열
# n일 동안 공부한 시간 합계를 '시:분' 형태의 문자열로 반환한다.
def solution(A):
    # total_time: n일 동안 공부한 시간 합계 (단위: 분)
    total_time = 0

    # A에 저장된 시간 목록을 순서대로 탐색하면서 total_time을 구한다.
    # 현재 탐색 중인 시간이 분 단위로 변환되어 t에 저장된다.
    for t in map(parse_log, A):
        total_time += t

    # total_time을 시간과 분 단위로 변환
    hour = total_time // 60
    minute = total_time % 60

    # 시간은 최소 2자리 이상, 분은 2자리로 표현한다.
    ret = ""
    if hour < 100:
        ret = "%02d:%02d" % (hour, minute)
    else:
        ret = "%d:%02d" % (hour, minute)
    return ret


A = list(input().split())
print(solution(A))

# 추가 문제: 백준 10821, 10822, 2908, 5622
