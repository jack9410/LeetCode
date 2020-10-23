# https://upcount.tistory.com/59 참고
# 다시 풀어보기
# 크기순으로 배열
# 첫번째 숫자 고정
# 나머지 둘숫자를 가장 작은 수와 큰수로 시작
# 범위를 좁혀가며 합이 0인 조합 저장

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
 
        ans, n = [], len(nums)        
        
        # 크기순으로 정렬
        nums.sort()
        # print(nums)
 
        for i in range(n) :
            
            # 시작수가 중복된 상황은 건너뛰기
            if i > 0 and nums[i] == nums[i-1] :
                continue
 
            # 범위 지정해서 탐색
            l, r = i+1, n-1

            while l < r :
                # print(nums[i], nums[l], nums[r])
                s = nums[i] + nums[l] + nums[r]
                
                # 0보다 작으면 왼쪽 키우기
                if s < 0 :
                    l += 1
                
                # 0보다 크면 오른쪽 줄이기
                elif s > 0 :
                    r -= 1

                # 0일떄
                else :
                    # 탐색 완료
                    ans.append([nums[l],nums[i],nums[r]])
                    
                    # 방금 저장한 조합이랑 같은 수일때 건너뛰기
                    while l < n-1 and nums[l] == nums[l+1] :
                        l += 1
                    while r > 1 and nums[r] == nums[r-1] :
                        r -= 1
                    
                    # 왼쪽 오른쪽 둘 다 키우고 줄이기
                    l += 1
                    r -= 1
 
        return ans