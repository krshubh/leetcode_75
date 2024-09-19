class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target + 1)
        i = 1
        while (i <=target) :
            for j in nums :
                if i == j :
                    dp[i] = dp[i] + 1
                else :
                    if i - j >= 0 :
                        dp[i] = dp[i] + dp[i-j]
                # print(i, j, dp)
            i += 1
        return dp[-1]
        