class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value_seen = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(max_value_seen, arr[i])
            arr[i] = max_value_seen
            max_value_seen = newMax
        return arr