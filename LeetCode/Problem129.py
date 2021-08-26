# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = []

    def sumNumbers(self, root: TreeNode) -> int:
        sum = 0
        
        self.runDFS(root)
        
        for res in self.result:
            print(res)
            sum += res

        return sum

    def runDFS(self, root):
        if root != None:
            self.result.append(self.toString(root.val) + self.toString(self.runDFS(root.right)))
            self.result.append(self.toString(root.val) + self.toString(self.runDFS(root.left)))
    
    def toString(self, val):
        if val == None:
            return ""
        else:
            return str(val)