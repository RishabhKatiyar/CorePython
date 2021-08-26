# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    root = None
    def maxDepth(self, root: TreeNode) -> int:
        depth = -1
        depth = max(depth, self.calculateDepth(root, 0))
        return depth

    def calculateDepth(self, root: TreeNode, current_level) -> int:
        left_depth = 0
        right_depth = 0
        if root:
            current_level += 1
            if root.left:
                left_depth = self.calculateDepth(root.left, current_level)
            if root.right:
                right_depth = self.calculateDepth(root.right, current_level)
        return max(left_depth, right_depth, current_level)

    def createTree(self, nodeList: list):
        nodeList.insert(0, -1)
        self.root = self.insertNode(nodeList, 1)
        return self.root

    def insertNode(self, nodeList: list, i: int):
        if i >= len(nodeList) or nodeList[i] == None:
            return None
        node = TreeNode()
        node.val = nodeList[i]
        node.left = self.insertNode(nodeList, i*2)
        node.right = self.insertNode(nodeList, i*2+1)
        return node

    def inOrderTraversal(self, node: TreeNode):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val, end = '\t')
            self.inOrderTraversal(node.right)

    def preOrderTraversal(self, node: TreeNode):
        if node:
            print(node.val, end = '\t')
            self.inOrderTraversal(node.left)
            self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node: TreeNode):
        if node:
            self.inOrderTraversal(node.left)
            self.inOrderTraversal(node.right)
            print(node.val, end = '\t')


root = [3, 9, 20, None, None, 15, 7]
#root = [1, 2, 3, 4, 5, None, None]
#root = [1, None, 2]
ob = Solution()
tree_root = ob.createTree(root)

'''
ob.inOrderTraversal(ob.root)
print()
ob.preOrderTraversal(ob.root)
print()
ob.postOrderTraversal(ob.root)
print()
'''
print(ob.maxDepth(ob.root))

