class Solution:
    def isHappy(self, n: int) -> bool:

        seen = {}

        while n != 1:
            n_sum = 0
            for d in str(n):
                n_sum += int(d)**2
            if n_sum not in seen:
                seen[n_sum] = True
            else:
                return False
            n = n_sum

        return True
                

        