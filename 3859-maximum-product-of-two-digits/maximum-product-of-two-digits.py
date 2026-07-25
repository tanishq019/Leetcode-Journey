class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]

        while n>0:
            arr.append(n%10)
            n//=10

        arr.sort(reverse=True)

        return arr[0]*arr[1]