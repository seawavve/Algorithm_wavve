class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res=len(S)
        l=0
        r=0
        
        for i in range(len(S)):
            if S[i]=='(': l+=1
            if l>0 and S[i]==')': 
                r+=2
                l-=1
                
        return res-r
