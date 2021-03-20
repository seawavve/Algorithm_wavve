class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #초기화
        res=numBottles
        tmp=1
        
        #몫은 tmp, 나머지는 rest
        while tmp>=1:
            tmp= (numBottles//numExchange)
            rest= (numBottles%numExchange)
            res+=tmp
            numBottles=tmp+rest
            
        return res
