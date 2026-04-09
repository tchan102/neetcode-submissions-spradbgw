class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(ch for ch in s.lower() if ch.isalnum())
        return t == t[::-1]