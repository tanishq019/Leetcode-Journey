class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0 = 0
        c1 = 0
        c2 = 0
        
        for x in stones:
            rem = x % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1

        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1

        diff = c1 - c2
        if diff < 0:
            diff = -diff
            
        return diff > 2