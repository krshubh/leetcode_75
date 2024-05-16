class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_index = nums.index(0) if 0 in nums else -1 
        if zero_index == -1 :
            product = 1
            for i in nums :
                product *= i
            return [int(product/i) for i in nums]
        else :
            temp = [0]*len(nums)
            product = 1
            for i in range(len(nums)) :
                if i != zero_index :
                    product *= nums[i]
            temp[zero_index] = int(product)
            return temp
        