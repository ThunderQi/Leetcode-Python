# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(i+1,len(nums)):
                if (nums[j] == temp):
                    return [i, j]
        return []
# @lc code=end

