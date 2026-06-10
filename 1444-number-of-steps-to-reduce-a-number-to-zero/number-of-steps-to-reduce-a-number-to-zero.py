class Solution:
    def numberOfSteps(self, num: int, count: int = 0) -> int:
        # Base case: we reached zero
        if num == 0:
            return count
        
        # Recurse based on even/odd status, incrementing count by 1
        if num % 2 == 0:
            return self.numberOfSteps(num // 2, count + 1)
        else:
            return self.numberOfSteps(num - 1, count + 1)