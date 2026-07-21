class Solution:
    def subarrayBitwiseORs(self, arr):
        res = []
        left = 0

        for num in arr:
            right = len(res)

            # Start new subarray [num]
            res.append(num)

            # Extend all subarrays ending at previous index
            for i in range(left, right):
                value = res[i] | num

                # Avoid consecutive duplicates
                if res[-1] != value:
                    res.append(value)

            left = right

        return len(set(res))