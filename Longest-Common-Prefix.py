# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def largest(self, strs):
        ans = ""

        if not strs:
            return ans

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return ans
            ans += char
        return ans

"""
Need to identify number of elements in list, so 'le'
need to see if first character, or first element, matches first character of other elements
if it doesn't, return ""
if it does, then check the first and second character of first element, then match other elements
and so on, until no match
finally return ans, which is number of matching elements
"""

"""Test Cases
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""

Input: strs = ["abab","aba","abc"]
Output: "ab"
"""

a = ["abab", "aba", "abc"]
Solution = Solution()
print(Solution.largest(a))
