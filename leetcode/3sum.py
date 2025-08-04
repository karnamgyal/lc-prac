class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
                
        list = []
        nums.sort()
        t = 0

        while t < len(nums):

            # Skip duplicate t values
            if t > 0 and nums[t] == nums[t - 1]:
                t += 1
                continue

            b, c = t + 1, len(nums) - 1
            while b < c: 
                if nums[b] + nums[c] == nums[t] * -1:
                    list.append([nums[t], nums[b], nums[c]])
                    b += 1
                    c -= 1

                    # Skip duplicates for b and c
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                        
                elif nums[b] + nums[c] < nums[t] * -1:
                    b += 1
                    
                elif nums[b] + nums[c] > nums[t] * -1:
                    c -= 1

            t += 1

        return list