# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Note:
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # My solution
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        value = root.val if root.val >= L and root.val <= R else 0
        if root.left != None:
            value += self.rangeSumBST(root.left, L, R)
        if root.right != None:
            value += self.rangeSumBST(root.right, L, R)
        return value

    # Better solution
    def rangeSumBST_solution(self, root: TreeNode, L: int, R: int) -> int:
        # second function so i don't have to pass around L and R in every recursive call
        def dfs(node):
            if L <= node.val <= R:
                self.ans += node.val
            if L <= node.val and node.left != None:
                dfs(node.left)
            if R >= node.val and node.right != None:
                dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

tn = TreeNode(10)
tn.left = TreeNode(5)
tn.left.left = TreeNode(3)

tn.right = TreeNode(5)
tn.right.right = TreeNode(3)
print(Solution().rangeSumBST_solution(tn, 5, 10))