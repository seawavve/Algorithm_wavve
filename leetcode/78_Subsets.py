class Solution:
    def subsets(self, nums):
        #초기화
        s=2**len(nums)
        res=[]
        r=[]
        
        for i in range(s):
            #'0'넣어 자리 맞추기
            bi=bin(i)[2:]
            if len(bi)<len(nums):
                for _ in range(len(nums)-(len(bi))):
                    bi='0'+bi
                    
            #'001'
            r=[]
            for j in range(len(nums)):
                if bi[j]=='1':
                    r.append(nums[j])
            res.append(r)
        
        return res
