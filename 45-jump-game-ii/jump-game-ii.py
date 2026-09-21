class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        reach=0
        end=0

        for i in range(n-1):
            reach=max(reach,i+nums[i])

            if reach>=n-1:
                ans+=1
                break

            if i==end:
                ans+=1
                end=reach

        return ans

        