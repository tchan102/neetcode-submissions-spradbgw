class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for k in s: 
            if k in table.keys():
                stack.append(table[k])
            elif stack and stack[-1] == k:
                stack.pop()
            else:
                return False
        return not stack