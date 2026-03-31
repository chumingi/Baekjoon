"""
자료구조:
- 정수: k
- 문자열: A

알고리즘:
- 문자열 A에 있는 문자 중, 임의의로 k개를 선택한 모든 부분 문자열을 tuple로 만든다.
  - 파이썬 combinations() 함수를 사용하면 된다.
- tuple을 문자열로 변환한다.
  - 파이썬의 join() 함수를 사용하면 된다.
- 만들어진 문자열을 오름차순으로 출력한다.
  - 파이썬의 sort() 함수를 사용하면 된다.
"""

# itertools 패키지에서 combinations() 함수를 가져온다.
from itertools import combinations


# A: 알파벳 소문자로 구성된 문자열
# C(A, k)를 정렬한 후, 배열 형태로 반환한다.
def solution(A, k):
    # 문자열 A에서 k를 선택하여 배열 B에 저장한다.
    B = list(combinations(A, k))
    # 배열 B에 저장된 tuple을 문자열로 반환한다.
    C = list("".join(b) for b in B)

    # 배열 C를 오름차순으로 정렬하고 반환한다.
    C.sort()
    return C


A = input()
k = int(input())
C = solution(A, k)
for c in C:
    print(c)

# 추가 문제: 백준 15649, 15650
