#DP
class Solution:
    def fib(self, N: int) -> int:
        l=[None]*31
        l[0]=0
        l[1]=1
        for i in range(2,N+1):
            l[i]=l[i-1]+l[i-2]
        return l[N]
            

#recursion
class Solution:
    def fib(self, N: int) -> int:
        if N==0: return 0
        if N==1: return 1
        return self.fib(N-1)+self.fib(N-2)
