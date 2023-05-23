# @before-stub-for-debug-begin
from python3problem20 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}", "(":")", "[":"]"}
        if (len(s) % 2 != 0) :
            return False
        bracketsArray = [s[0]]
        for i in range(1,len(s)):
            temp = s[i]
            len_array = len(bracketsArray)
            if (len(bracketsArray) == 0) :
                bracketsArray.append(s[i])
                continue
            if brackets.get(s[i]) is None:
                if (brackets.get(bracketsArray[len_array - 1]) == s[i] ) :
                    bracketsArray.pop()
                else :
                    bracketsArray.append(s[i])
            else :
                bracketsArray.append(s[i])
        if (len(bracketsArray) == 0) :
            return True
        else :
            return False
# @lc code=end

