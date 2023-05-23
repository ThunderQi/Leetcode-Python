#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)) :
            temp = roman_num[s[i]]
            if (i < (len(s)-1) and temp < roman_num[s[i+1]]) :
                result += 0 - temp 
            else :
                result += temp 

        return result
# @lc code=end

