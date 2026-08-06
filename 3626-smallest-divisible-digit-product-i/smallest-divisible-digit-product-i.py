class Solution:

  def smallestNumber(self, n: int, t: int) -> int:
    for i in range(n, 101):
      temp = i
      prod = 1  
      while temp > 0:
        prod *= temp % 10
        temp //= 10

      if prod % t == 0:
        return i

    return n