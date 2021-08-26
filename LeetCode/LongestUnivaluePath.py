# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.func(root)
        return self.longest
    
    def func(self, node: TreeNode) -> int:
        if node == None:
            return 0
        leftP, rightP = self.func(node.left), self.func(node.right)
        left = (leftP + 1) if node.left and node.val == node.left.val else 0
        right = (rightP + 1) if node.right and node.val == node.right.val else 0
        self.longest = max(self.longest, left + right)
        return max(left, right)