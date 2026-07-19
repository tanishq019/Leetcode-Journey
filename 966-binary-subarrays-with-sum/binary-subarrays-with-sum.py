class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            if goal<0: return 0

            l,summ,ans=0,0,0

            for r in range(len(nums)):
                summ+=nums[r]

                while summ>goal:
                    summ-=nums[l]
                    l+=1

                ans+=(r-l+1)

            return ans

        return atmost(goal)-atmost(goal-1)