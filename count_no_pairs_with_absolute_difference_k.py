class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = 0
        start = 1
        for i in range(len(nums)):
            for j in range(start,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    pairs += 1
            start += 1
        return pairs
