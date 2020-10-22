class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            second = target - nums[idx]
            
            if (second in nums):
                sec_idx = nums.index(second)
                if sec_idx != idx:
                    return [idx, sec_idx]
                