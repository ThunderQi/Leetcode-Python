# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums与nums[:]区别待进一步debug进行分析，两种形式在服务器侧执行结果不同，本地执行执行结果相同
        nums[:] = sorted(set(nums))
        return len(nums)
# @lc code=end

