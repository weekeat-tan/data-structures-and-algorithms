'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''

# Intuition:
# We want to determine if the iteration ends up in a cycle, or becomes 1. This is implicitly a Linked List with Cycle problem.
# We could make use of a fast and slow pointer algorithm, with the slow pointer moves forward with just 1 step and the fast pointer moves by 2 steps.
# When we detect the slow pointer is the same as the fast pointer, we break out of the loop.
# Then, determine if the number is a happy number.
# If fast pointer equals to 1, it is a happy number. Otherwise, it is not a happy number.
#
class Solution:
    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total
    
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if slow == fast:
                break
        return fast == 1