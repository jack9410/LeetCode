class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        goal = len(nums)-1
        
        if goal == 0:
            return True
        
        avail_idx = 0
        
        for i in range(goal):
            jump_idx = i + nums[i]
            avail_idx = max(avail_idx, jump_idx)
            if avail_idx >= goal:
                    return True
            if avail_idx == i and nums[avail_idx] == 0:
                return False
            if avail_idx < i:
                return False
            