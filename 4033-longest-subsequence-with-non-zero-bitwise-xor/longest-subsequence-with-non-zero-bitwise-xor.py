class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for x in nums:
            total_xor ^= x
            
        if total_xor != 0:
            return len(nums)
        if any(nums):
            return len(nums) - 1
        return 0