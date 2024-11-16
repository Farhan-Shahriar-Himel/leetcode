class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return 0
            
        jumps = i = 1
        r = tr = nums[0]
    
        while r < len(nums) - 1:
            if i == r:
                tr = max(tr, i + nums[i])
                if r < tr:
                    r = tr
                    jumps += 1
            tr = max(tr, i + nums[i])
            i += 1
    
        
        return jumps