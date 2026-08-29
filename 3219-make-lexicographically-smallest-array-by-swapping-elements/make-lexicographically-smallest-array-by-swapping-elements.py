class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_nums = sorted(nums)

        num_to_group = {}
        groups = []
        
        group_idx = 0
        groups.append([sorted_nums[0]])
        num_to_group[sorted_nums[0]] = group_idx
        
        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                group_idx += 1
                groups.append([])
            
            groups[group_idx].append(sorted_nums[i])
            num_to_group[sorted_nums[i]] = group_idx

        group_head = [0] * len(groups)

        res = [0] * n
        for i in range(n):
            val = nums[i]
            grp = num_to_group[val]

            res[i] = groups[grp][group_head[grp]]
            group_head[grp] += 1
            
        return res