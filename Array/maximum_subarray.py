class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = nums[0]
        max_sum = nums[0]
        left_i = 1
        while(left_i < len(nums)) :
            temp_sum += nums[left_i]
            if temp_sum <= 0 :
                if nums[left_i] > 0 and temp_sum <= 0:
                    temp_sum = nums[left_i]
                elif nums[left_i] < 0 and nums[left_i] > temp_sum :
                    temp_sum = nums[left_i]
                else :
                    temp_sum = 0
            else :
                if nums[left_i] > temp_sum :
                    temp_sum = nums[left_i]
            if temp_sum > max_sum :
                max_sum = temp_sum
            left_i += 1
            print(max_sum)
        return max_sum
        