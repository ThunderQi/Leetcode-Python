#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        length = - len(digits)
        for i in range(len(digits)) :
            if ( i == 0) :
                digits[-i -1] = digits[-i -1] + 1
            if (digits[-i - 1] + carry > 9) :
                digits[-i - 1] = 0 
                carry = 1
            else :
                digits[-i - 1] = digits[-i - 1] + carry
                carry = 0
                break
        if (carry == 1) :
            digits.insert(0,1)
        return digits
# @lc code=end

