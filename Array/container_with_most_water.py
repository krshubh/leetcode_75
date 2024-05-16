class Solution:
    def waterVolume(self, left_index, right_index, array):
        return min(array[left_index], array[right_index])*(right_index - left_index)

    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) -1
        max_water_volume = 0
        while (left_index < right_index):
            new_water_volume = self.waterVolume(left_index, right_index, height)
            if new_water_volume > max_water_volume :
                max_water_volume = new_water_volume
            if height[left_index] > height[right_index] :
                right_index -= 1
            else :
                left_index += 1
        return max_water_volume
