#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    bracket_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            print(c)
            if c in self.bracket_map.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if self.bracket_map[open] != c:
                    return False
        return len(stack) == 0




# @lc code=end

