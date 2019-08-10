# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.


class Solution:
    def findPairs(self, nums, k):
        if k < 0: return 0
        pairs = []
        numbersFound = {}
        for num in nums:
            upper = num + k
            upperPair = (num, upper)
            lower = num - k
            lowerPair = (lower, num)

            if (upper in numbersFound) and (upperPair not in pairs):
                pairs.append(upperPair)

            if (lower in numbersFound) and (lowerPair not in pairs):
                pairs.append(lowerPair)

            if num not in numbersFound:
                numbersFound[num] = True

        return len(pairs)

# https://www.journaldev.com/20806/python-counter-python-collections-counter
import collections
class BetterSolution: # FASTER
    def findPairs(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

        #the same as above
                # wow
        # c = collections.Counter(nums)
        # return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)

print(BetterSolution().findPairs([1, 2, 3, 4, 5], -1)) # 0


# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
print(Solution().findPairs([3, 1, 4, 1, 5], 2))
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
print(Solution().findPairs([1, 2, 3, 4, 5], 1))
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
print(Solution().findPairs([1, 3, 1, 5, 4], 0))

