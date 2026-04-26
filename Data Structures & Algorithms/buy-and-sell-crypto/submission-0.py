class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1.Brute Force
        # max = 0

        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if(prices[j]>prices[i]):
        #             diff = prices[j] - prices[i]
        #             if(diff>max):
        #                 max = diff
        #                 print(diff)
        
        # return max


        #2. Two Pointer
        l,r = 0, 1
        maxProfit = 0

        while(r<len(prices)):
            if(prices[l]<prices[r]):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l=r
            r+=1
        return maxProfit

        