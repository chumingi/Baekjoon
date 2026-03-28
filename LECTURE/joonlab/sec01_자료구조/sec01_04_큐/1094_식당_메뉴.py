"""
자료구조:
- 정수: n
- 문자 배열: s
- 큐: q
알고리즘:
- 배열 s에 저장된 몬든 원소 s_i를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 s_i를 이용하여 정답을 구한다.
- 새로운 학생이 식당에 도착한 경우, 학생 번호와 좋아하는 메뉴를 큐에 넣는다.
- 식사 1인분이 준비된 경우, z에서 학생 1명을 제거하고, 학생이 좋아하는 메뉴와 준비된 메뉴를 비교하여 정답을 갱신한다.
- q에 있는 학생은 식사를 못한 것으로 간주한다.
- 전답으로 구한 학생들을 학생 번호 기준으로 오름차순으로 정렬한다.
"""

from collections import deque


# 나의 풀이
def solution(n, s):
    q = deque()
    A, B, C = [], [], []

    for info in s:
        if info[0] == 1:
            q.append([info[1], info[2]])
        else:
            if q[0][1] == info[1]:
                A.append(q[0][0])
            else:
                B.append(q[0][0])
            q.popleft()

    if q:
        for x in q:
            C.append(x[0])
    return [A, B, C]


n = int(input())
s = list(list(map(int, input().split())) for _ in range(n))
ret = solution(n, s)
for c in ret:
    c.sort()
    if len(c) == 0:
        print("None")
    else:
        print(*c)


# n, s: n개의 정보가 저장된 s
# - 1 a b: 학생 번호가 정수 a이고 선호하는 메뉴가 정수 b인 학생 1명이 식당 입구에 도착한다.
# - 2 b: 메뉴가 정수b인 식사 1인분이 준비된다.
def solution1(n, s):
    # answer: [[학생 목록 A], [학생 목록 B], [학생 목록 C]]
    answer = [[] for _ in range(3)]

    # 식당 입구에서 대기 중인 학생 번호를 저장하는 큐(덱)
    q = deque()

    # n개의 정보를 순서대로 처리한다.
    for info in s:
        # 학생이 식당 입구에 도착함. 식당 입구에서 대기 중인 학생이 1명 증가한다.
        # q의 맨 뒤에 학생 번호와 좋아하는 메뉴를 넣는다.
        if info[0] == 1:
            q.append((info[1], info[2]))
        # 식사 1인분이 준비된다.
        # 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 한다.
        # 즉, 큐의 맨 앞에 잇는 학생 1명이 식사를 시작한다.
        else:
            a, b = q.popleft()
            # a번 학생이 좋아하는 메뉴를 먹는 경우
            if b == info[1]:
                answer[0].append(a)
            # a번 학생이 좋아하지 않는 메뉴를 먹는 경우
            else:
                answer[1].append(a)

    # 식사를 못하는 학생을 answer[2]에 넣는다.
    while len(q) > 0:
        a, b = q.popleft()
        answer[2].append(a)

    # 학생 번호 기준으로 오름차순 정렬한다.
    for i in range(3):
        answer[i].sort()
    return answer


n = int(input())
s = list(list(map(int, input().split())) for _ in range(n))
T = solution1(n, s)
for t in T:
    if len(t) == 0:
        print("None")
    else:
        for x in t:
            print(x, end=" ")
        print()

# 추가 문제: 백준 2164, 12873, 1966
