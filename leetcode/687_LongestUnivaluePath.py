# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #클래스 변수 선언
    res: int = 0
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def DFS(node):
            if node is None:return 0
            
            #DFS
            left=DFS(node.left)
            right=DFS(node.right)
            
            #거리계산
            if (node.left) and (node.left.val == node.val):
                left+=1
            else:left=0
            if (node.right) and (node.right.val == node.val):
                right+=1
            else:right=0
            
            #최댓값이 결과
            self.res=max(self.res,left+right)
            return max(left,right)
        
        DFS(root)
        return self.res
