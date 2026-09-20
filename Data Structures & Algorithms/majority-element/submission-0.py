class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}

        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        return max(counter, key=counter.get)
        