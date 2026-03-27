"""
자료구조:
- 정수: n, m
- 문자열 배열: A
- 문자열: B
- 딕셔너리: D
알고리즘:
- 배열 A의 모든 원소 x_i, y_i를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다. x_i는 i번째 원소의 물건 이름, y_i는 i번째 원소의 물건 가격이다.
- 현재 탐색 중인 원소 x_i, y_i를 이용하여 딕셔너리 D를 만든다. 딕셔너리 D의 키는 물건 이름 x_i, 값은 물건 가격 y_i이다.
- 문자열 B에 저장된 모든 원소 b를 첫번째 원소부터 마지막 원소까지 순서대로 탐색한다.
- 현재 탐색 중인 원소 b의 물건 가격의 합을 구한다. b의 물건 가격은 딕셔너리 D를 이용하여 D[b]로 얻을 수 있다.
"""


# n, A: 가게에서 판매하는 물건 목록 정보
# m, B: 구매하려는 물건 목록 정보
def solution(n, A, m, B):
    # D: {키=물건이름, 값=물건 가격} 형태의 딕셔너리
    # A에 저장된 물건 목록 정보를 이용하여 D를 만든다.
    D = {}
    for name, cost in A:
        D[name] = int(cost)

    # B에 저장된 모든 물건의 물건 가겨의 합을 구한다.
    answer = 0
    for name in B:
        answer += D[name]

    return answer


n, m = map(int, input().split())
A = list(list(input().split()) for _ in range(n))
B = list(input().split())
print(solution(n, A, m, B))

# 추가 문제: 백준 5089
