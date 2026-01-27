class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b =[]*2
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i]+nums[j]==target):
                    b.append(i)
                    b.append(j)

        return b

