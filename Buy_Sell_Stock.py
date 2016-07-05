'''Q16 - Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)


Example 2:
In this case, no transaction is done, i.e. max profit = 0.
Input: [7, 6, 4, 3, 1]
Output: 0
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """       
        # Brute Force - O(n^2)
        profit = 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if(prices[j] > prices[i] and profit < prices[j] - prices[i]):
                    profit = prices[j] - prices[i]
        return profit
                
        #Optimized - O(n)
        max_profit , min_price = 0,float('inf')
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(max_profit,profit)
        return max_profit

