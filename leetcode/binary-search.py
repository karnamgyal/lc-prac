class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1;

        while low <= high:

            middle = low + (high - low) // 2
            value = nums[middle]

            if value < target:
                low = middle + 1 
            elif value > target: 
                high = middle - 1;
            else:
                return middle;
        return -1