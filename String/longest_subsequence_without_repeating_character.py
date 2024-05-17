class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        result = r - l
        ss = ''
        while r != len(s) :
            if s[r] not in ss :
                ss += s[r]
                r += 1
            else :
                l = (r - len(ss)) + list(ss).index(s[r]) + 1
                ss = s[l:r] + s[r]
                r += 1
            if len(ss) > result :
                result = len(ss)
        return result