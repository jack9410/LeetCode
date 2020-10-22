from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        N = len(nums)
        
        idx_lst = list(range(N))
        
        for idx in range(N):
            second = target - nums[idx]
            if second not in nums:
                continue
            else:
                sec_idx = nums.index(second)
                return [idx, sec_idx]
            
            
        