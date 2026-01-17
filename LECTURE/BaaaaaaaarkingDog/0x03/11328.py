""" 입력
첫째 줄: 테스트 케이스의 수 0 < N < 1001
각각의 테스트 케이스: 하나의 줄에 영어 소문자들로만 이루어진 두 개의 문자열이 한 개의 공백으로 구분되어 주어짐.
각각의 문자열의 길이: 최대 1000"""
""" 출력
각각의 테스트 케이스에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지의 여부를
"Impossible"(불가능) 또는 "Possible"(가능)으로 따옴표는 제외하고 출력"""

from collections import Counter
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
for i in range(N):
    first, second = input().split()
    write("Possible\n") if Counter(first) == Counter(second) else write("Impossibln")

""" 시간복잡도: O(N * M log M)
- N: 테스트케이스 수 (최대 1000)
- M: 문자열 길이 (최대 1000)
- 정렬 시 O(M log M) → 각 테스트케이스마다 정렬 1회"""
""" 공간복잡도: O(M)
- 정렬 or Counter에 문자열 하나 저장
- 문자열 길이만큼의 임시 배열이 사용됨"""