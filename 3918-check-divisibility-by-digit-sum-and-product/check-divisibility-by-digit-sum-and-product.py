class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        original = n
        while n > 0 :
            last_digit = n % 10
            summ += last_digit
            prod *= last_digit
            n //= 10
        return original % (summ + prod) == 0