class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value_seen = -1
        temp_value = 0
        for i in range(len(arr)-1, -1, -1):
            temp_value = arr[i]
            arr[i] = max_value_seen
            max_value_seen = max(max_value_seen, temp_value)
        return arr