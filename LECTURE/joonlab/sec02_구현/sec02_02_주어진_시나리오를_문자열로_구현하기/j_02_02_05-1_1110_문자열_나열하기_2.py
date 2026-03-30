"""더 생각하기
P[A] 중에서 사전 순으로 k번째 문자열을 출력하려면 어떻게 할까?
PA에서 k번째 문자열만 반환하면 된다.
"""

from itertools import permutations


# A: 알파벳 소문자로 구서오딘 문자열
# 문자열 A의 P[A] 중에서 사전 순으로 k번째 문자열을 반환한다.
def solution(A, k):
    # 문자열 A를 정렬된 1차원 배열로 변환한후, (sorted() 함수)
    # 정렬된 문자열 A로 변환한다. (join() 함수)
    A = "".join(sorted(A))

    # 정렬된 문자열 A에 있는 모든 문자의 순열을 오름차순으로 생성하여 PA에 저장한다.
    # - permutations() 함수가 문자열 A에 대한 모든 순열을 오름차순으로 생성한다.
    PA = []
    for p in permutations(A):
        PA.append("".join(p))
    return PA[k - 1]


A, k = list(input().strip().split())
print(solution(A, int(k)))
