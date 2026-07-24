class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        last = m + n -1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while m > 0:
            nums1[last] = nums1[m-1]
            m -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

        #[1,2,10,20,20,40]    
        # m = 4, n = 2, last 5
        #[10,20,20,40,0,0] [1,2]

        #[10,20,20,40,0,40] [1,2]
        # m = 3, n = 2, last 4
        
        #[10,20,20,40,20,40] [1,2]
        # m = 2, n = 2, last 3
        
        #[10,20,20,20,20,40] [1,2]
        # m = 1, n = 2, last 2
        
        #[10,20,10,20,20,40] [1,2]
        # m = 0, n = 2, last 1

