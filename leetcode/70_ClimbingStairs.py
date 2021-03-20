class Solution:
    def climbStairs(self, n: int) -> int:
        l=[0]*47
        l[1]=1
        l[2]=2
        for i in range(1,n):
            l[i+2]=l[i+1] + l[i]
        return l[n]
        
