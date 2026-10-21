class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)
        seen=set()
        repeated=0
        missing=0
        
        for num in nums:
            if num in seen:
                repeated=num
            else:
                seen.add(num)
        for num in range(1,n*n+1):
            if num not in seen:
                missing =num
        return [repeated,missing]