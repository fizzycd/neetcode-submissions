class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
        L, R = 0, 0
        zeros = 0
        longest_seq = 0
        while R < len(nums):
            if nums[R] == 0:
                zeros += 1
            while zeros == 2:
                if nums[L] == 0:
                    zeros -= 1
                L += 1
            
            longest_seq = max(longest_seq, R - L + 1)
            R += 1
        
        return longest_seq


