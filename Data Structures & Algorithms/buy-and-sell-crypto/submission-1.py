class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Left = 0 # Left will point to our current smallest price
        maxProfit = 0

        for Right in range(Left, len(prices)):
            currentProfit = prices[Right] - prices[Left]
            maxProfit = max(maxProfit, currentProfit)

            if prices[Right] < prices[Left]:
                Left = Right

        return maxProfit
            
        

        