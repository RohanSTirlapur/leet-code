from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        dp = [0] * (budget + 1)

        for factor, price in items:
            count = 0

            for f, _ in items:
                if f % factor == 0:
                    count += 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + count)

        ans = 0

        for spent in range(budget + 1):
            ans = max(ans, dp[spent] + (budget - spent) // min_price)

        return ans