"""
자료구조:
- 정수: n
- 정수형 배열: A
- 딕셔너리: D
알고리즘:
- 배열 A의 모든 원소 a_i를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 a_i를 이용하여 딕셔너리 D를 만든다. 딕셔너리 D의 키는 수 a_i, 값은 수 a_i의 출현 횟수이다.
- 딕셔너리 D의 값 중에서 최댓값을 구한다. 딕셔너리 D의 값이 앞에서 구한 최댓값과 같은 모든 키를 배열에 저장하고, 배열을 오름차순으로 정렬한다.
"""


# n, A: n개의 양의 정수가 저장된 1차원 배열 A
# 배열 A에서 출현 회수가 가장 많은 수를 오름차순으로 저장한 배열을 반환한다.
def solution(n, A):
    # D: {key=수, value=수의출현횟수}
    # mx: D에서 출현 횟수의 최댓값을 저장
    # 배열 A의 모든 원소에 대한 출현 횟수를 D에 반영한다.
    mx = 0
    D = {}
    for a in A:
        if a in D:
            D[a] += 1
        else:
            D[a] = 1
        mx = max(mx, D[a])

    # D[key] = mx인 모든 key를 answer에 저장한다.
    answer = []
    for key, value in D.items():
        if value == mx:
            answer.append(key)
    answer.sort()
    return answer


n = int(input())
A = list(map(int, input().split()))
B = solution(n, A)
for b in B:
    print(b, end=" ")
# print(*B)  # 시간 더 빠름

# 추가 문제: 백준 1920
