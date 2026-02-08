"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        mapping = {')': '(', '}': '{', ']': '['}
        stk = []

        for char in s:
            if char in mapping.values():
                stk.append(char)
            elif char in mapping:
                if not stk or mapping[char] != stk.pop():
                    return False

        return not stk
    