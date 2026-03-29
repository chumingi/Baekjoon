"""
자료구조:
- 정수: n, m
- 문자열 배열: A (학생의 선호도 저장), B (질의 저장)
알고리즘:
- 배열 B에 저장된 질의 b_i를 첫번째 질의부터 m번째 질의까지 순서대로 탐색한다.
- 현재 탐색 중인 b_i에 대해, b_i와 일치하는 배열 A의 원소 개수를 구한다.
- 배열 A의 모든 원소 a_i를 탐색하면서, b_i와 일치하는 a_i의 개수를 구하면 된다.
"""


# n, A: n명 학생의 선호도 조사 결과가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
def solution(n, m, A, B):
    # 배열 B에 저장된 m개의 질의를 순서대로 처리한다.
    answer = []
    for subject in B:
        # subject이 '-'인 경우, 전체 학생 수 n을 answer에 넣는다.
        if subject == "-":
            answer.append(n)
        # subject를 선택한 학생 수를 구하여 answer에 넣는다.
        else:
            cnt = 0
            for a in A:
                if a == subject:
                    cnt += 1
            answer.append(cnt)

    return answer


n, m = map(int, input().split())
A = list(input().split())
B = list(input().strip() for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)
