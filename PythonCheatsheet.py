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

    # to get the quotient and the remainder
    quotient, remainder = divmod(2578, 10) # returns (257, 8) => quotient: 257, remainder: 8

''' String '''
# Converting list to string
"".join(["a", "b", "c"])
"".join(str(element) for element in [1, 2, 3])


''' List '''
reversed(["a", "b", "c"]) # Return the list in the reversed order.
["a", "b", "c"].reverse() # Reverse the order of the list

''' Sorting '''
num = [1,2,3,4]

# Sorting that is in-place (the list itself is modified) and stable (the order of two equal elements is mainted), using Timsort.
# TC: O(n log n)
# SC: O(n)
num.sort()