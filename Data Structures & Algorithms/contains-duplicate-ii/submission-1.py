class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dups = {}

        for i in range(len(nums)):
            if nums[i] not in dups:
                dups[nums[i]] = i
            elif i - dups[nums[i]] <= k:
                return True
            else:
                dups[nums[i]] = i
                
        return False

        
        