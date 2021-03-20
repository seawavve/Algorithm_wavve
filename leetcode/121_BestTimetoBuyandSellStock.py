class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        #초기화
        buy=[ ]
        profit=[ ]
        
        #buy:낮은 값으로 밀기
        tmp=prices[0]
        for i in range(len(prices)):
            if tmp>prices[i]: tmp=prices[i]
            buy.append(tmp)
        #profit: prices-buy값
        for j in range(len(prices)):
            profit.append(prices[j]-buy[j])
            
        return max(profit)
