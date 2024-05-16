class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:] :
            temp_sum += num
            temp_sum = max(num, temp_sum)
            max_sum = max(max_sum, temp_sum)
        return max_sum