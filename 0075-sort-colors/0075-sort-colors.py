class Solution:
    def sortColors(self, nums: list[int]) -> None:

        n=len(nums)
        count0=0
        count1=0
        count2=0

        for num in nums:
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else:
                count2+=1
        i=0
        for j in range(count0):
            nums[i]=0
            i+=1
        for j in range(count1):
            nums[i]=1
            i+=1
        for j in range(count2):
            nums[i]=2
            i+=1
        