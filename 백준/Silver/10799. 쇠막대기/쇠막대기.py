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