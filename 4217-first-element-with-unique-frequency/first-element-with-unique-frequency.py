class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        freq=Counter(nums)
        freq_count=Counter(freq.values())

        for num in nums:
            if freq_count[freq[num]]==1:
                return num

        return -1