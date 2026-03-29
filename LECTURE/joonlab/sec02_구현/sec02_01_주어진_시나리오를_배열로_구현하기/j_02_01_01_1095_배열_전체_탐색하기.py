"""
자료구조:
- 정수: n, m
- 정수형 배열: A, B
알고리즘:
- 배열 B에 있는 질의 k_i를 첫번째 질의부터 m번째 질의까지 순서대로 탐색한다.
- 현재 탐색 중인 k_i에 대해, 배열 A에서 원소의 값이 k_i보다 크거나 같은 원소의 개수를 구한다.
- 배열 A의 모든 원소 a_i를 탐색하면서, k_i보다 크거나 같은 a_i의 개수를 구하면 된다.
"""


# n, A: n개의 정수가 저장된 1차원 배열 A
# m, B: m개의 질의가 저장된 1차원 배열 B
# m개의 질의 처리 결과를 순서대로 저장하여 배열 형태로 반환한다.
def solution(n, m, A, B):
    # m개의 질의를 순서대로 처리한다. 현재 질의 정보는 k에 저장된다.
    # answer: m개의 질의 결과를 순서대로 저장하는 배열
    answer = []
    for k in B:
        # 배열 A의 첫번째 원소부터 마지막 원소까지 순서대로 탐색하면서,
        # 배열 A에서 k보다 크거나 같은 원소의 개수를 변수 cnt에 저장한다.
        cnt = 0
        for a in A:
            if a >= k:
                cnt += 1

        # cnt에 저장된 값을 answer의 끝에 추가한다.
        answer.append(cnt)

    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)

""" 더 생각하기
n, m의 최댓값이 100,000인 경우,
위 알고리즘의 시간 복잡도는 O(n*m)으로,
최악의 경우 10**10 번의 연산이 필요하다.
10**8번의 연산에 1초가 걸린다고 가정하면,
100초로 시간초과가 발생한다.
"""

# 추가 문제: 백준 10818, 2562
