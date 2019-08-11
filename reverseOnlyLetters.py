# 917. Reverse Only Letters
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 

# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "

# My Solution
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        notLetters = {}
        for i, char in enumerate(S):
            if char.isalpha():
                stack.append(char)
            else:
                if char not in notLetters:
                    notLetters[char] = []
                notLetters[char].append(i)

        returnList = [None for _ in range(len(S))]
        for k, v in notLetters.items():
            for index in v:
                returnList[index] = k
            

        for i in range(len(S)):
            if returnList[i] == None:
                returnList[i] = stack.pop()
        
        return "".join(returnList)


#  duh
class BetterSolution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

print(Solution().reverseOnlyLetters("ab-cd4f-h"))