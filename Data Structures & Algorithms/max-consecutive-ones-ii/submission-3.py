class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        before = 0
        after = 0
        seen_zero = 0
        res = 0

        for num in nums:
            if seen_zero == 1:
                if num == 1:
                    after += 1
                else:
                    res = max(res, before + after + 1)
                    before = after
                    after = 0

            if seen_zero == 0:
                if num == 1:
                    before += 1
                else:
                    seen_zero += 1
        if seen_zero == 0:
            return before
        
        res = max(res, before + after + 1)        
        return res



    # 1, 0, 1, 0
    # 0, 1, 0, 1
    # 0, 0
    # 1, 1
    # 1, 0
    # 0, 1


        