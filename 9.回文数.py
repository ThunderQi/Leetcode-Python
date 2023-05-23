# @before-stub-for-debug-begin
from python3problem9 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        len_x = len(str_x)
        for i in range(len_x) :
            if (i > len_x/2):
                break
            if (str_x[i]!=str_x[len_x-i-1]):
                return False
        return True
# @lc code=end

