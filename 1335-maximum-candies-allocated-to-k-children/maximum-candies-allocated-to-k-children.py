class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high=1,max(candies)
        ans=0

        while low<=high:
            mid=low+(high-low)//2

            children=sum(pile//mid for pile in candies)

            if children>=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1

        return ans