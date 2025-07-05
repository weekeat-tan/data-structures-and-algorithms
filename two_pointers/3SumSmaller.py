'''
Given an array of n integers nums and an integer target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example 1:
    Input: nums = [-2,0,1,3], target = 2
    Output: 2
    Explanation: Because there are two triplets which sums are less than 2:
        [-2,0,1]
        [-2,0,3]

Example 2:
    Input: nums = [], target = 0
    Output: 0

Example 3:
    Input: nums = [0], target = 0
    Output: 0
'''

# Intuition:
# 1. Use 3 pointers to point to the current element, next element and the last element.
# 2. Since the array is not sorted, we need to sort the array so we know how we can move the pointer correctly.
# 3. For the next and the last element, it can be simplified to find the number of pairs with nums[next] + nums[last] < target - nums[current]
# 3.1. To find the number of pairs, we can start with a left pointer at current element + 1 and a right pointer at the last element.
# 3.2. While there is no matching sum, move the right pointer to the left one by one.
# 3.3. Once found, get the count by right - left.
#
# TC: O(n^2), sorting takes O(n log n) and two loops take O(n^2)
# SC: O(1), no additional space is used
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            # find the number of pairs, starting from i+1 to len(nums)-1, that is smaller than target - nums[i]
            count += self.twoSumSmaller(i+1, nums, target-nums[i])
        return count
    
    def twoSumSmaller(self, startIdx: int, nums: List[int], target: int) -> int:
        count = 0
        lo, hi = startIdx, len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                count += hi - lo
                lo += 1 # increment left pointer to find the next set of possible pairs
            else:
                hi -= 1
        return count