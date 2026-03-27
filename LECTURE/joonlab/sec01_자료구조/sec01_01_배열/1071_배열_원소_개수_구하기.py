# n, A: 원소의 개수가 n인 정수형 배열 A
# 배열 A의 원소 중에서 값이 k인 원소의 개수를 반환한다.
def solution(n, A, k):
    # 배열 A의 모든 원소를 탐색하면서 원소의 값이 k와 같으면
    # answer를 1만큼 증가시킨다.
    answer = 0
    for a in A:
        if a == k:
            answer += 1
    return answer


# 입력을 받고 정답을 출력한다.
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(solution(n, A, k))

# 추가 문제: 백준 10807, 10871
