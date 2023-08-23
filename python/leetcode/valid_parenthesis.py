# https://leetcode.com/problems/valid-parentheses/

# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()

                    if c == ")" and top != "(":
                        return False
                    
                    if c == "}" and top != "{":
                        return False
                    
                    if c == "]" and top != "[":
                        return False

        return len(stack) == 0
