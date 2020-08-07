# nums = [2,3,1,1,4]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]


def canJump(self, nums) -> bool:
    if len(nums) == 1:
        return True
    
    goal = len(nums)-1
    stack = []
    stack.append(0)
    
    while stack:
        node_idx = stack.pop()
        tmp = 0
        for i in range(1, nums[node_idx] + 1):
            if node_idx + i == goal:
                return True
            elif nums[node_idx + i] == 0:
                continue
            else:
                stack.append(node_idx + i)
        # print(stack)
    return False

print(canJump(nums))