"""
자료구조:
- 정수:
  - n, m
  - 정수형 배열: A, B
  - psum: 유형 1의 질의 결과를 누적 합 개념을 이용하여 저장
  - psum2: 유형 2를 빠르게 처리하기 위해 배열 A에 대한 누적 합을 저장

알고리즘:
- 배열 B에 있는 모든 질의 b_i를 순서대로 탐색하면서 질의 b_i를 처리한다.
- 질의 b_i가 유형 1이면,
  - A[i]부터 A[j]까지의 배열 A의 원소에 k를 더한다.
  - 누적 합 개념을 이용하여 psum[i]를 k만큼 증가시키고, psum[j+1]를 k만큼 감소시켜서 O(1)에 빠르게 처리한다.
- 질의 a_i가 유형 2이면,
  - A[i]부터 A[j]까지의 합을 출력한다.
  - 누적 합 개념을 이용하여 psum[1]부터 psum[n-1]까지 순서대로 배열 psum의 값을 누적하여 더한다.
  - 그 후에 psum의 값을 배열 A에 순서대로 더한다.
- psum2[i]에 A[0..i]의 누적 합을 저장한다.
- A[i]부터 A[j]까지의 합은 psum2[i-1] - psum2[j]로 O(1)에 빠르게 구할 수 있다.
"""


# n, A: 크기가 n인 정수형 1차원 배열
# m, B: m개의 질의 (질의 융형: 1, 2)를 저장한 배열
# 유형 2의 질의 결과를 순서대로 한 줄씩 출력한다.
def solution(n, m, A, B):
    # psum: 유형 1에 대한 누적 합 배열 (모든 원소의 초깃값: 0)
    # psum: 유형 2를 위한 배열 A에 대한 누적 합 배열 (모든 원소의 초깃값 0)
    # - psum2[i] = A[0] + A[1] + ... + A[i]
    # psum_flag: psum, psum2, A 배열이 완성되면 True, 그렇지 아니면 False를 저장한다.
    psum = [0] * n
    psum2 = [0] * n
    psum_flag = False

    # m개의 질의를 순서대로 처리한다.
    for b in B:
        if b[0] == 1:
            do_add_query(psum, b[1], b[2], b[3])
        else:
            # psum 배열을 이용하여 A, psum2를 완성한다. (최초 1회 수행됨)
            if psum_flag == False:
                # psum 배열을 완성한다.
                psum_flag = True
                for i in range(1, n):
                    psum[i] += psum[i - 1]

                # psum을 A에 더한다.
                for i in range(n):
                    A[i] = A[i] + psum[i]

                # psum2를 만든다.
                psum2[0] = A[0]
                for i in range(1, n):
                    psum2[i] = psum2[i - 1] + A[i]

            # A[b[1]] + ... A[b[2]] 값을 출력한다.
            # (A[0] + ... + A[b[2]]) - (A[0] + ... + A[b[1] - 1])과 동일하다.
            if b[1] == 0:
                print(psum2[b[2]])
            else:
                print(psum2[b[2]] - psum2[b[1] - 1])


# i부터 j까지의 배열 A의 원소에 k를 더한다.
# 누적 합을 이용하여 O(1)에 처리한다.
def do_add_query(psum, i, j, k):
    psum[i] += k
    if j + 1 < n:
        psum[j + 1] -= k


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, A, B)

# 추가 문제: 백준 11659, 16139, 11441
