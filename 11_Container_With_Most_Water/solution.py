from itertools import combinations
class Solution(object):
    def maxArea(self, height):
        max_area = 0
        a = len(height)
        index = [ i for i in range(a)]
        comb_lst  = list(combinations(index, 2))
        print(comb_lst)
        for i in comb_lst:
            fir_idx = i[0]
            sec_idx = i[1]

        return max_area
    

