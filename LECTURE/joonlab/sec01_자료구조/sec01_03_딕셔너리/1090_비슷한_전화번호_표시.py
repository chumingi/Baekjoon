"""
자료구조:
- 정수: n
- 문자열: A ,B
- 딕셔너리: D
알고리즘:
- 문자열 A에 있는 모든 전화번호 a_i를 첫번째 전화번호부터 마지막 전화번호까지 순서대로 탐색한다.
- 현재 탐색 중인 a_i에 대하여, 자기 자신을 제외한 모든 접두사 x_i를 탐색한다.
- 현재 탐색 중인 x_i를 이용하여, 딕셔너리 D를 만든다. 딕셔너리 D의 키는 접두사 x_i, 값은 접두사 x_i의 출현 횟수이다.
- D를 이용하여 문자열 B의 출현 횟수를 구한다.
"""


# A: n개의 전화번호가 공백으로 구분되어 저장된 문자열
# B: 하나의 전화번호가 저장된 문자열
# 문자열 A에 포함된 전화번호 중 문자열 B를
# 자기 자신을 제외한 접두사로 갖는 전화번호의 개수를 반환한다.
def solution(A, B):
    # D: {key=자기자신을제외한접두사, value=출현횟수} 형태의 딕셔너리.
    # 문자열 A에 저장된 모든 전화번호를 탐색하면서, 탐색 중인
    # 전화번호에 대해 자기 자신을 제외한 접두사를 이용하여 D를 만든다.
    # 참고로, D[B]만 필요하기 때문에, 딕셔너리가 아닌 정수형 변수를 사용하여
    # x가 B와 같을 때만 관리하면 효율적이다. 하지만, 딕셔너리 연습을 위해 D를 사용한다.
    D = {}
    for phone in A:
        # 전화번호 phone의 모든 접두사의 출현 횟수를 1만큼 증가시킨다.
        # 전화번호 phone는 제외
        for i in range(len(phone) - 1):
            x = phone[: i + 1]
            if x in D:
                D[x] += 1
            else:
                D[x] = 1

    # 문자열 A에 포함된 전화번호 중, 문자열 B를
    # 자기 자신을 제외한 접두사로 갖는 전화번호가 없으면 0을 반환한다.
    if B in D:
        return D[B]
    else:
        return 0


A = list(input().split())
B = input()
print(solution(A, B))


# 나만의 풀이
def solution2(A, B):
    answer = 0
    for a in A:
        if a != B and a.startswith(B):
            answer += 1
    return answer


A = list(input().split())
B = input()
print(solution2(A, B))

# 추가 문제: 백준 18679, 11478
