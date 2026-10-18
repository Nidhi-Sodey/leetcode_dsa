class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer=[1]*(len(nums))
        left=1
        for i in range(len(nums)):
            answer[i]=answer[i]*left
            left=left*nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]=answer[i]*right
            right=right*nums[i]
        return answer
            