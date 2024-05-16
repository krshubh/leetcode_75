class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSoFar = minSoFar = result = 1
        for i in range(0, len(nums)):
            curr = nums[i]
            tempMaxSoFar = max(curr, maxSoFar * curr, minSoFar * curr)
            minSoFar = min(curr, maxSoFar * curr, minSoFar * curr)
            maxSoFar = tempMaxSoFar
            result = max(maxSoFar, result)

        return result