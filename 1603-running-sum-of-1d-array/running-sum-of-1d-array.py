class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        result = []
        for i in range(len(nums)):
            sums = sums + nums[i]
            result.append(sums)
        return result
        