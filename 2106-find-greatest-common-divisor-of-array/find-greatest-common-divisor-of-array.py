class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n  = len(nums)
        nums.sort()
        small = nums[0]
        large = nums[n-1]
        i = small
        while i > 0:
            if large % i == 0 and small % i == 0:
                return i
            i = i-1
        return 1
       
        