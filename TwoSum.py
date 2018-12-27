#!/usr/bin/env python3
#-*-coding:utf8-*-

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution():
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(len(self.nums))
        list(enumerate(self.nums))
        for dice1,num1 in enumerate(self.nums):
            for dice2,num2 in enumerate(self.nums):
                if num2==target-num1 and num1 != num2 and num2>num1:
                    return [dice1,dice2]

nums = [2,7,11,15]
target = 9
solution = Solution(nums,target)
print(solution.twoSum())