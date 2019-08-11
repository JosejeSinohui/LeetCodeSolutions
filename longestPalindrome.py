# 409. Longest Palindrome
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# My Solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        result = 0
        foundExtra = False
        for count in counts.values():
            if count % 2 == 0:
                result += count
            else:
                if not foundExtra:
                    result+=1
                    foundExtra = True
                result += count - 1
        return result


from collections import Counter
class BetterSolution:
    def longestPalindrome(self, s):
        ans = 0
        for v in Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans