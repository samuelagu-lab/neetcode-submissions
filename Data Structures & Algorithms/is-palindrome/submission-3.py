class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            il = s[i].lower()
            jl = s[j].lower()
            if (ord(il) < 97 or ord(il) > 122) and (ord(il) < 48 or ord(il) > 57):
                i += 1
                continue 
            if (ord(jl) < 97 or ord(jl) > 122) and (ord(jl) < 48 or ord(jl) > 57):
                j -= 1
                continue
            if il != jl:
                return False
            i += 1
            j -= 1
        
        return True        