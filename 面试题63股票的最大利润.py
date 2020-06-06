class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        min_price = prices[0]
        result = 0
        for price in prices:
            min_price = min(price,min_price)
            result = max(result,price-min_price)
        return result

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))