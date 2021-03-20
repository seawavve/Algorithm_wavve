class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #초기화
        mat=[[0 for col in range(N+1)] for row in range(N+1)]
        for ii in range(len(trust)):
            mat[trust[ii][0]][trust[ii][1]]=1
        
        #검사
        for j in range(1,N+1):
            c=0
            for i in range(1,N+1):
                if mat[i][j]==1:c+=1
                if c==N-1:
                    for k in range(1,N+1):
                        if mat[j][k]==1:return -1
                    return j
        return -1
            
