class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_val = 0
        for i in nums:
            if i == 1:
                counter += 1
                if counter > max_val:
                    max_val = counter
            else:
                counter = 0
        return max_val