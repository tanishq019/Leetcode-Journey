class Solution:
    def missingInteger(self, A: list[int]) -> int:
        n = len(A)
        seen = set(A)
        summ = A[0]

        for i in range(1, n):
            if A[i] == A[i - 1] + 1:
                summ += A[i]
            else:
                break

        while summ in seen:
            summ += 1

        return summ