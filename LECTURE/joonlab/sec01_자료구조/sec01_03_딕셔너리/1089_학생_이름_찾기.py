"""
자료구조:
- 정수: n, m
- 문자열: A, B
- 딕셔너리: D
알고리즘:
- 문자열 B에 있는 모든 학생 b_i를 첫번째 학생부터 마지막 학생까지 탐색한다.
- 현재 탐색 중인 b_i를 이용하여 딕셔너리 D를 만든다. 딕셔너리 D의 키는 학생이름 b_i, 값은 학생 이름 b_i의 출현 횟수이다.
- 문자열 A에 있는 모든 학생 a_i를 첫번째 학생부터 마지막 학생까지 순서대로 탐색한다.
- 현재 탐색 중인 a_i 중에서 딕셔너리 D에 존재하지 않는 모든 a_i를 배열로 만들고, 만들어진 배열을 오름차순으로 정렬한다.
"""


# A: n개의 학생 이름이 공백으로 구분된 문자열
# B: m개의 학생 이름이 공백으로 구분된 문자열
def solution(A, B):
    # D: {key=학생이름, value=출현횟수} 형태의 사전
    # B에 저장된 학생 이름을 순서대로 처리하면서 D를 만든다.
    D = {}
    for b in B:
        if b in D:
            D[b] += 1
        else:
            D[b] = 1

    # A에 저장된 학생 이름 중에서 D에 없는 학생 이름을 answer에 넣는다.
    answer = []
    for a in A:
        if a not in D:
            answer.append(a)
    answer.sort()
    return answer


A = list(input().split())
B = list(input().split())
C = solution(A, B)
for c in C:
    print(c)

# 추가 문제: 백준 1764, 15098, 10815, 1269
