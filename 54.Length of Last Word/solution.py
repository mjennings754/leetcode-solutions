"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
"""
Steps taken:
you'll want to strip all the whitespace and split into words. If there are no words return 0. Return the length of the last word
[-1] - negative indexing to access the last element
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        if not words:
            return 0

        return len(words[-1])