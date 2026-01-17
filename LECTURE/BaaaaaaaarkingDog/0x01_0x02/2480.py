a, b, c = map(int, input().split())
if (a == b == c):
    print(10000 + a*1000)
elif (a==b or a==c):
    print(1000 + a*100)
elif (b==c):
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)

# 시간 복잡도: O(1): 입력 크기가 고정되어 있으며, 조건문과 최대값 계산이 일정한 시간 내에 수행
# 공간 복잡도: O(1): 세 개의 정수형 변수만 사용되며, 추가적인 데이터 구조가 필요하지 않음