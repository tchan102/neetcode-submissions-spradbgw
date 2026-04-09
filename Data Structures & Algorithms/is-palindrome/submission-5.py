class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = [ch for ch in s.lower() if ch.isalnum()]
        return k == k[::-1]