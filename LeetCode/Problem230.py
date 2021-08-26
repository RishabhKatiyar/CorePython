# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    count = 0
    k = 0
    result = -1
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.k = k
        self.inOrderTraversal(root)
        return self.result

    def inOrderTraversal(self, node: TreeNode):
        if node and self.result == -1:
            self.inOrderTraversal(node.left)
            self.count += 1
            if self.count == self.k:
                self.result = node.val
                return
            self.inOrderTraversal(node.right)

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

root = [3, 1, 4, None, 2]
ob = Solution()
tree_root = ob.createTree(root)

print(ob.kthSmallest(ob.root, 2))