class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        max_area = (right-left) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1
            max_area = max(max_area, (right-left) * min(height[left], height[right]))

        return max_area

sol = Solution()
print('answer =', sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))

