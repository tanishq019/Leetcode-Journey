class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        dup = []
        for i in nums:
            if i in s:
                dup.append(i)
            else:
                s.add(i)

        return dup