class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        invalid_char = [' ', ',', '.', ':', '@', '#', '_', '\'', '\"', 
                        '{', '}', '[', ']', '(', ')', '-', '?', ';',
                        '!', '\\', '`']
        for c in s :
            if c not in invalid_char :
                new_s += c
        return new_s == new_s[::-1]
        