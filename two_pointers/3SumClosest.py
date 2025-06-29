'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

# Intuition:
#   Similar to 3Sum problem, use 3 pointers to point the current element, next element and the last element.
#   Since the array is not sorted, we need to sort the array first.
#   If the sum (i.e., nums[current] + nums[left] + nums[right]) is less than target, it means we have to add a larger element so next element move to the right.
#   If the sum is greater than target, it means we have to add a smaller element so last element move to the left. 
#   Keep doing this until the end. Each time compare the difference between the sum and target,
#       if the difference is less than minimum difference so far, then replace the result with it, otherwise keep iterating.
#
# TC: O(n^2) where n is the legnth of the input array
# - Sorting takes O(n log n) time, and two loops of the array makes O(n^2) which dominates the time complexity.
# SC:  O(n) where n is the length of the input array
# - Sorting takes O(n) space.
from math import inf

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort() # O(n log n)
        smallest_diff = inf
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                target_diff = target - sum
                if abs(target_diff) < abs(smallest_diff) \
                    or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff): # this is only required if we want the smaller value given the same absolute difference
                   smallest_diff = target_diff
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
        return target - smallest_diff
