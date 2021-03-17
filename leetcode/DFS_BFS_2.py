# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9

input   [4,2,7,1,3,6,9]
stdout  [4, 7, 9, 6, 2, 3, 1]
        [4, 2, 7, 1, 3, 6, 9]


'''
class Solution:
    DFS_list: list= [ ]
    BFS_list: list= [ ]
        
    def Search(self, root: TreeNode) -> TreeNode:
        if root is None:return 0
        
        def DFS(root):
            stack=collections.deque([root])
            
            while stack:
                tmp=stack.pop()
                self.DFS_list.append(tmp.val)
                if tmp.left:stack.append(tmp.left)
                if tmp.right:stack.append(tmp.right)
                    
        def BFS(root):
            queue=collections.deque([root])
            
            while queue:
                tmp=queue.popleft()
                self.BFS_list.append(tmp.val)
                if tmp.left:queue.append(tmp.left)
                if tmp.right:queue.append(tmp.right)
        DFS(root)
        print(self.DFS_list)
        BFS(root)
        print(self.BFS_list)
        
        

