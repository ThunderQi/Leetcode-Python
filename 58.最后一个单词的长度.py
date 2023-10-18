# @before-stub-for-debug-begin
from python3problem58 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
# @lc code=end

