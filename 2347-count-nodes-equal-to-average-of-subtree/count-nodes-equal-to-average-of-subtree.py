# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            if node is None:
                return 0, 0
            
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            
            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1
            
            average = totalSum // totalCount
            
            if node.val == average:
                self.count += 1
            
            return totalSum, totalCount
        
        dfs(root)
        
        return self.count