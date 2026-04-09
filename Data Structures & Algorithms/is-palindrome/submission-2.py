class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [ch for ch in s.lower() if ch.isalnum()]
        L = 0
        R = len(t) - 1
        while L < R:
            if t[L] != t[R]:
                return False
            L += 1
            R -=1 

        return True