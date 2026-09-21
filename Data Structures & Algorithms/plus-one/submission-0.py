class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digit = "".join([str(i) for i in digits])

        plus_one = str(int(digit) + 1)

        return [int(i) for i in plus_one]
        