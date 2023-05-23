# @before-stub-for-debug-begin
from python3problem14 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1,len(strs)):
            if (result == "") :
                return ""
            strs_len = len(strs[i])
            result_len = len(result)
            if (strs_len >= result_len) :
                temp = strs[i][:result_len:]
            else :
                temp = result[:strs_len:]
                result = strs[i]
                result_len = len(result)
            for j in range(len(result)+1) :
                res = result[:result_len - j:]
                if (result[:result_len - j:] == temp[:result_len - j:] or res == "") :
                    result = res
                    break
        return result
# @lc code=end

