#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while (nums.count(val) > 0) :
            nums.remove(val)
        return len(nums)
# @lc code=end

