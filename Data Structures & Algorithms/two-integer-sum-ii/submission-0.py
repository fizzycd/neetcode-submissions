class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in seen:
                return [seen[comp], i + 1]
            seen[n] = i + 1
        return []