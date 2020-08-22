from itertools import combinations

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        itmes = [i for i in range(length)]
        comb_lst = list(combinations(items, 2))

    print(maxArea([1,8,6,2,5,4,8,3,7]))