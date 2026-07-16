class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxx = 0

        for i in range(len(nums)):
            maxx = max(maxx, nums[i])
            nums[i] = gcd(maxx, nums[i])

        nums.sort()

        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            ans += gcd(nums[left], nums[right])
            left += 1
            right -= 1

        return ans