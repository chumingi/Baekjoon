"""
자료구조:
- 정수: n
- 문자열: S
- 딕셔너리: D
알고리즘:
- 문자열 S에 저장된 모든 학생 이름 s_i를 첫번째 학생부터 마지막 학생까지 순서대로 탐색한다.
- 현재 탐색 중인 s_i를 이용하여 딕셔너리 D를 만든다. 딕셔너리 D의 키는 학생 이름 s_i, 값은 학생 이름 s_i의 출현 횟수이다.
- 딕셔너리 D를 [학생이름, 출현 횟수]를 원소로 갖는 배열로 변환하고, 변환된 배열을 학생 이름 기준으로 오름차순으로 정려한다.
"""


# S: 학생 이름이 공백으로 구분된 문자열
def solution(S):
    # D: {key=학생이름, value=출현횟수} 형태의 딕셔너리
    # S에 저장된 학생 이름을 순서대로 처리하면서 D를 만든다.
    D = {}
    for s in S.split():
        if s in D:
            D[s] += 1
        else:
            D[s] = 1

    # answer: [학생이름, 출현횟수]를 원소로 갖는 1차원 배열
    # 학생 이름 기준으로 오름차순으로 정렬한다.
    answer = list(D.items())
    answer.sort(key=lambda x: x[0])
    return answer


S = input()
A = solution(S)
for name, value in A:
    print(name, value)

# 추가 문제: 백준 10816, 14425
