class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        k = s.lower()
        while l < r:
            while not k[l].isalnum() and l < r:
                l += 1
            while not k[r].isalnum() and l < r:
                r -= 1
            if k[l] != k[r]:
                return False
            l += 1
            r -= 1
        return True