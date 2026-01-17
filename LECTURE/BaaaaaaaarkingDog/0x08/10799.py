"""
쇠막대기들이 긴 것 위에 작은 것이 겹쳐져 있다.
레이저: 인접괄호 ()
쇠막대기 양끝은 (과 )
괄호 표현식 주어졌을 때 잘려진 쇠막대기의 총 수를 구하기

괄호 문자열 길이 <= 100,000
"""

stack = []
is_laser = False
tot_cnt = 0

input_str = input().strip()
for ch in input_str:
    if ch == '(':
        is_laser = True
        stack.append(ch)
    else: # ch == ')
        stack.pop()
        if is_laser:
            is_laser = False
            tot_cnt += len(stack)
        else:
            tot_cnt += 1
print(tot_cnt)
            