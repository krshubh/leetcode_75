class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']' : '[', '}' : '{'}
        stack = []
        is_valid = True
        for c in s :
            if c in ['(', '[', '{'] :
                stack.append(c)
            elif c in [')', ']', '}'] :
                if len(stack) > 0 and stack[-1] == d[c] :
                    stack.pop()
                else :
                    is_valid = False
                    break
        if len(stack) > 0 :
            is_valid = False
        return is_valid