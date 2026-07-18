class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        swaps = 0
        n = len(row)

        for i in range(0,n,2):
            partner = row[i] ^ 1
            if row[i+1] != partner:
                for j in range(i+1,n):
                    if row[j] == partner:
                        partner_idx = j
                        break
                row[i+1], row[partner_idx] = row[partner_idx], row[i+1]
                swaps += 1
                
        return swaps
