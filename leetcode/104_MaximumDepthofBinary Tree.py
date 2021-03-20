# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #초기화
        res=0
        queue=collections.deque([root])
        if root==None:return 0
        
        #BFS
        while queue:
            res+=1
            for _ in range(len(queue)):
                im=queue.popleft()
                if im.left:
                    queue.append(im.left)
                if im.right:
                    queue.append(im.right)
        return res

