class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        letters = []
        word1_flag = True
        word2_flag = False

        while i < len(word1) and j < len(word2):
            if word1_flag:
                letters.append(word1[i])
                i += 1
                word1_flag = False
                word2_flag = True
            elif word2_flag:
                letters.append(word2[j])
                j += 1
                word1_flag = True
                word2_flag = False

        if j < len(word2) :
            return "".join(letters) + word2[j:]
        else:
            return "".join(letters) + word1[i:]




        