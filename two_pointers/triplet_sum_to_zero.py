'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
    
Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
'''

'''
Intuition:
    To fix the current iterating number, nums[i], and get two numbers that sum up to -num[i].
    We can use two sum to find the values that sum up to -nums[i].

Logic:
    1. Sort the nums array.
    2. Loop through the entire array.
    3. Find the two sum of the inverse of the current iterating number, i.e., nums[j] + nums[k] = -nums[i]
    4. Since we do not want duplicate, we can skip any iterating number that is the same as the previous iterating number, i.e., nums[i] == nums[i-1]
'''

# TC: O(n^2) where n is the length of the input array
# - Sorting takes O(n log n) time, and outer loops takes O(n) time and inner loop takes O(n) time.
# 
# SC: O(n) where n is the length of the input array 
# - Sorting takes O(n) space, do not count O(n^2) space for the output
class Solution:
    def searchPairs(self, nums: list[int], i: int, triplets: list[list[int]]):
        start, end = i + 1, len(nums) - 1
        while start < end:
            sum = nums[i] + nums[start] + nums[end]
            if sum == 0:
                triplets.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                
                # skipping repeating numbers to avoid duplicates
                # we can just increment the left pointer because a distinct element on the left pointer would never form a pair with the element on the right pointer
                while start < end and nums[start] == nums[start-1]:
                    start += 1
            elif sum < 0:
                start += 1
            else:
                end -= 1

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            # small optimisation: if the value is greater than zero, there is no way to form any triplets that sum to zero.
            if nums[i] > 0:
                break
            # skipping repeating number to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.searchPairs(nums, i, triplets)
        return triplets
