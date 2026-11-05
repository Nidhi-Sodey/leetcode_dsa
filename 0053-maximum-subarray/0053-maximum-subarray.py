class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        MaxSum=nums[0]
        CurrSum=0
        for num in nums:
            CurrSum+=num
            MaxSum=max(CurrSum,MaxSum)

            if CurrSum<0:
                CurrSum=0
        return MaxSum
