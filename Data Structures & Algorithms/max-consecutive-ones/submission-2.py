class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0
        for i in nums:
            if i == 1:
                counter += 1
                if counter > max:
                    max = counter
            else:
                if counter > max:
                    max = counter
                counter = 0
        return max