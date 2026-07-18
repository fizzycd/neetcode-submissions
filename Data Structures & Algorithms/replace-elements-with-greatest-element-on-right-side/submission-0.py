class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range((len(arr)-1)):
            r_numbers = arr[i+1:]
            greatest = max(r_numbers)
            arr[i] = greatest
        arr[-1] = -1
        return arr