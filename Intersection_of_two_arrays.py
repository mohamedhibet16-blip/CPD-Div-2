class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_arr = []
        for i in nums1:
            if i in nums2 and i not in new_arr:
                new_arr.append(i)
        return new_arr
