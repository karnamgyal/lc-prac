class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max(), return max value between arguments
        # min(), return min value between arguments
        a, b = 0, len(height) - 1
        max_area = 0

        while a < b:
            h = min(height[a], height[b])
            width = b - a
            max_area = max(max_area, h * width)

            if height[a] < height[b]:
                a += 1
            else: 
                b -= 1
        return max_area