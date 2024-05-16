class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        temp = n
        while temp != 0 :
            result = result + [i + 1 for i in result]
            temp = temp // 2
        return result[:n+1]