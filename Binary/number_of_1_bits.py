class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in bin(n)[2:] :
            if i == '1' :
                result += 1
        return result