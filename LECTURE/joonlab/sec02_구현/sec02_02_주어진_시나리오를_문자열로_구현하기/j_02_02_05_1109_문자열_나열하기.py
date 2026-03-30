"""
자료구조:
- 문자열 : A
알고리즘:
- 문자열 A에 있는 모든 문자를 오름차순으로 정렬하여 배열에 순서대로 저장한다.
  - 파이썬의 sorted() 함수를 사용한다.
- 앞에서 정렬된 배열의 모든 순열을 문자열로 구하고, 순서대로 출력한다.
  - permutations() 함수를 이용하여 배열의 모든 순열을 배열 형태로 만들고,
  - sorted() 함수를 이용하여 만들어진 배열을 문자열로 변환한다.
"""

from itertools import permutations


# A: 알파벳 소문자로 구성된 문자열
# 문자열 A에 대한 P(A)를 반환한다.
def solution(A):
    # 문자열 A를 정렬된 1차원 배열로 변환한후, (sorted() 함수)
    # 정렬된 문자열 A로 변환한다. (join() 함수)
    A = "".join(sorted(A))

    # 정렬된 문자열 A에 있는 모든 문자의 순열을 오름차순으로 생성하여 PA에 저장한다.
    # - permutations() 함수가 문자열 A에 대한 모든 순열을 오름차순으로 생성한다.
    PA = []
    for p in permutations(A):
        PA.append("".join(p))
    return PA


A = input()
PA = solution(A)
for a in PA:
    print(a)

""" 더 생각하기 (준렙 1110, 1112) """
