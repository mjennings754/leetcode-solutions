"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]

"""
s[:] creates a shallow copy of a sequence, s[::-1] -1 gets the entire string and reverses it.
"""