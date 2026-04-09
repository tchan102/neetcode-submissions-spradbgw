class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letters = [0] * 26
        
        for ch_s, ch_t in zip(s, t):
            letters[ord(ch_s) - ord('a')] += 1
            letters[ord(ch_t) - ord('a')] -= 1

        return not any(letters)