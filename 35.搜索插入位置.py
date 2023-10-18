#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (nums.count(target) > 0):
            return nums.index(target)
        else :
            #二分查找
            bisect.insort(nums, target)
            return nums.index(target)
# @lc code=end

