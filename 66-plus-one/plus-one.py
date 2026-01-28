class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = "".join([str(num) for num in digits])
        sumi = int(total)+1
        digi = [int(d) for d in str(sumi)]
        return digi