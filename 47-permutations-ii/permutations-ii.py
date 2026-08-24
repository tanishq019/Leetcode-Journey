class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        res = []
        path = []
        
        def backtrack():

            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in count:
                if count[num] > 0:
                    
                    count[num] -= 1
                    path.append(num)

                    backtrack()

                    path.pop()
                    count[num] += 1
                    
        backtrack()
        return res