class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1 and nums[0] == target:
            return 0

        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = l + 1
            elif nums[mid] > target:
                r = r - 1
            else:
                return mid

        return -1
        