# 입력: 첫째 줄에는 수열의 크기 n (1 <= n <= 1,000,000), 둘째 줄에는 수열, 셋째 줄에는 x (1 <= x <= 2,000,000)이 주어진다
# 출력: a_i + a_j = x (a <= i <= j <= n)을 만족하는 (a_i, a_j) 쌍의 개수를 출력한다.

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

exist = [0] * (x - 1)
i_j = 0
for i in arr:
    if x > i:
        if exist[x - i - 1] == 1:
            i_j += 1
        else:
            exist[i - 1] += 1
print(i_j)