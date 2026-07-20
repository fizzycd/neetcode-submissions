class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            if c in bracket_mapping:
                if not stack or stack.pop() != bracket_mapping[c]:
                    return False
                
        return not stack