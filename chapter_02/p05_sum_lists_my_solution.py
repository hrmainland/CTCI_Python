# My solution to p05_sum_lists.py
def sum_lists(ll_a, ll_b):
    count = 0
    left = ll_a.head
    right = ll_b.head
    step = 0
    while True:
        if not left and not right:
            return count
        if left:
            left_val = left.value
            left = left.next
        else:
            left_val = 0
        if right:
            right_val = right.value
            right = right.next
        else:
            right_val = 0
        count += left_val * right_val * pow(10, step)
        step += 1
        

# 617
# 295

# 912

# 716
# 592


# [9,1,2]

# [2, 1, 9] 
# 12
# 10
# 8

# 12 + 100 + 800