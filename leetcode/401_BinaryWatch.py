class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        s=1024
        hour=None
        minute=None
        res=[]
        
        
        for i in range(s):
            #'0010100000' 10자리 맞추기
            bi=bin(i)[2:]
            if len(bi)<10:
                for _ in range(10-len(bi)):
                    bi='0'+bi
            
            if bi.count('1')==num:
                hour=int(bi[:4],2)
                if hour>11:continue
                minute=int(bi[4:],2)
                if minute>59:continue
                if minute<10:
                    minute='0'+str(minute)
                else:minute=str(minute)
                res.append(str(hour)+':'+minute)
        return res
