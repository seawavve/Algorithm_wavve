# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #class변수 선언
    res: int=0
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def DFS(root):
            if root is None:res=0
            stack=collections.deque([root])
            
            while stack:
                tmp=stack.pop()
                if (L<=tmp.val) and (tmp.val<=R):self.res+=tmp.val
                if tmp.left:stack.append(tmp.left)
                if tmp.right:stack.append(tmp.right)
        DFS(root)
        return self.res
                
