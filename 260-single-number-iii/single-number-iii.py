class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ele_count=Counter(nums)
        ans=[]

        for val,count in ele_count.items():
            if count==1:
                ans.append(val)

        return ans