class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters = {}

        for c in s:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
        print(letters)
        for c in t:
            if c in letters:
                letters[c] -= 1
            else:
                return False
            if letters[c] == -1:
                return False
        
        return sum(letters.values()) == 0 
        