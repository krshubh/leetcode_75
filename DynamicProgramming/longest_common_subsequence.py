def lcs(S1, S2, m, n):
    # Returns length of LCS for S1[0..m-1], S2[0..n-1]
    if m == 0 or n == 0:
        return 0
    if S1[m - 1] == S2[n - 1]:
        return 1 + lcs(S1, S2, m - 1, n - 1)
    else:
        return max(lcs(S1, S2, m, n - 1),
                    lcs(S1, S2, m - 1, n))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        S1 = text1
        S2 = text2
        m = len(S1)
        n = len(S2)
        return lcs(S1, S2, m, n)
        