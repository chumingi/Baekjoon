"""
자료구조:
- 문자열 A
알고리즘:
- 문자열 A의 lower() 함수를 이용하여 대문자를 소문자로 변환한다.
"""


# A: 알파벳 대소문자로 구성된 문자열
# 문자열 A의 모든 대문자를 해당 대문자에 대응하는 소문자로 치환한 문자열을 반환
def solution(A):
    B = A.lower()
    return B


A = input()
print(solution(A))
