class Solution:
    def countCommas(self, n: int) -> int:
        result=0
        for i in range(1,n+1):
            if i>999:
                result+=1
        return result