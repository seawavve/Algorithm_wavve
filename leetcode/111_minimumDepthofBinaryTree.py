class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:return 0
        queue=deque([root])
        res=0
        
        while queue:
            res+=1
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left is None and node.right is None: 
                    return res
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
        return res
