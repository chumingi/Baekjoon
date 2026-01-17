"""
문제 2: 주어진 길이 N인 int 배열 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면 
1, 존재하지 않으면 0을 반환하는 함수 int func2(int arr[], int N)을 작성하라. 단,
arr의 각 수는 0 이상 100 이하 N은 1000 이하

func2({1, 52, 48}, 3)     => 1  // 52 + 48 = 100
func2({50, 42}, 2)        => 0  // 합 100 불가능
func2({4, 13, 63, 87}, 4) => 1  // 13 + 87 = 100
"""

def func2(arr, N):
    for i in range(0, N-1):
        for j in range(i+1, N):
            if (arr[i] + arr[j] == 100):
                return 1
    return 0

print(func2([1, 52, 48], 3))
print(func2([50, 42], 2))
print(func2([4, 13, 63, 87], 4))

ㅔ갸ㅜㅅ("\n시간복잡도: O(N^2)")