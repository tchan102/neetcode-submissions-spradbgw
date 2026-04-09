class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for ch in s: 
            if ch in table:
                stack.append(table[ch])
            elif stack and stack[-1] == ch:
                stack.pop()
            else:
                return False
        return not stack