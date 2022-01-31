class Solution:
    def fib(self, n: int) -> int:
        #상향식 풀이법(Tabulation)
        dp=[0,1]+[0]*(n-1)
        for idx in range(2,n+1):
            dp[idx]=dp[idx-1]+dp[idx-2]
        return dp[n]
        
        # 하향식 풀이법(Memoizarion)
        if n<=0: return 0
        elif n==1: return 1
        return self.fib(n-1) + self.fib(n-2)
