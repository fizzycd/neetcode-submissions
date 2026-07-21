class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        parsed = ''
        for char in s:
            if char.isalnum():
                parsed += char
        for i in range(len(parsed)):
            if parsed[i] != parsed[-1-i]:
                return False
        return True

        