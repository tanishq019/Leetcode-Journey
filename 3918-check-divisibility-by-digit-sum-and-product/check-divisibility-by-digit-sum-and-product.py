class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        temp = n
        while n > 0 :
            last_digit = n % 10
            summ += last_digit
            prod *= last_digit
            n //= 10
        total = summ + prod
        if temp % total == 0:
            return True
        else:
            return False