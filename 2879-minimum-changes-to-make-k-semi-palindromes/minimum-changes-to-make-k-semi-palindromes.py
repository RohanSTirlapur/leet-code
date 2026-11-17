
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[l][r] = minimum changes to make s[l:r+1]
        # a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        # Precompute minimum changes
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):
                        left = l + offset
                        right = l + offset + ((length - 1 - offset) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[l][r] = min(cost[l][r], changes)

        # Dynamic Programming
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):
                    if dp[parts - 1][j] != INF:
                        dp[parts][i] = min(
                            dp[parts][i],
                            dp[parts - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]

        