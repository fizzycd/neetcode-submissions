class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        sub_sum = 0
        res = 0
        for R in range(len(arr)):
            sub_sum += arr[R]
            if R - L + 1 > k:
                sub_sum -= arr[L]
                L += 1
            if R - L + 1 == k:
                if sub_sum >= threshold * k:
                    res += 1
        
        return res