'''
I/O
'''
in_val = input()
int_num = int(in_val)
float_num = float(in_val)


''' Number '''
def number():
    from math import inf
    num = inf

    # or simply
    num = float("inf")


'''
Sorting
'''
num = [1,2,3,4]

# Sorting that is in-place (the list itself is modified) and stable (the order of two equal elements is mainted), using Timsort.
# TC: O(n log n)
# SC: O(n)
num.sort()