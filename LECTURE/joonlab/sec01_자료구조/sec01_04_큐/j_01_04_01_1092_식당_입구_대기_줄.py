"""
자료구조:
- 정수: n
- 문자열 배열: A
- 큐: q
알고리즘:
- 배열 A에 저장된 모든 원소 a_i를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 a_i를 이용하여 정답을 구한다. 새로운 학생이 식당에 도착한 경우, 학생 번호를 q에 넣는다.
- 식사 1인분이 준비된 경우, q에서 1개의 학생 번호를 제거한다.
"""

from collections import deque


# n, A: n개의 정보가 저장된 배열
# - 1 a: 학생 번호가 a인 학생 1명이 식당 입구에 도착한다.
# - 2: 식사 1인분이 준비된다.
def solution(n, A):
    # answer: [대기하는 학생 수의 최댓값, 이 때 맨 뒤에 대기 중인 학생 번호]
    answer = [0, 0]

    # 식당 입구에서 대기 중인 학생 번호를 저장하는 큐(덱)
    q = deque()

    # 배열 A에 저장된 n개의 정보를 순서대로 처리한다.
    for info in A:
        # 학생이 식당 입구에 도착함. 대기 중인 학생 1명 증가
        if info[0] == 1:
            # 큐의 맨 끝에 학생번호를 삽입하고, 정답을 갱신한다.
            # 식당 입구의 맨 뒤에 대기 중인 학생 번호는 info[1]이다.
            q.append(info[1])
            if answer[0] < len(q) or (answer[0] == len(q) and answer[1] > info[1]):
                answer = [len(q), info[1]]

        # 식사 1인분이 준비된다.
        # 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 한다.
        # 큐의 맨 앞에 있는 학생 번호를 삭제한다.
        else:
            q.popleft()

    return answer


n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))
B = solution(n, A)
print(B[0], B[1])

# 추가 문제: 백준 2161, 11866
