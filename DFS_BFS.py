class Solution:
    #클래스 변수 선언
    DFS_list: list= [ ]
    BFS_list: list= [ ]
        
    def TreeSearch(self, root: TreeNode) -> int:
        #DFS
        def DFS(node):
            if node is None:return 0
            self.DFS_list.append(node.val)
            left=DFS(node.left)
            right=DFS(node.right)
            
        #BFS
        def BFS(node):
            if node is None:return 0
            queue=collections.deque([node])
            while queue:
                for _ in range(len(queue)):
                    tmp=queue.popleft()
                    self.BFS_list.append(tmp.val)
                    if tmp.left:
                        queue.append(tmp.left)
                    if tmp.right:
                        queue.append(tmp.right)
        DFS(root)
        print(self.DFS_list)
        BFS(root)
        print(self.BFS_list)
        
