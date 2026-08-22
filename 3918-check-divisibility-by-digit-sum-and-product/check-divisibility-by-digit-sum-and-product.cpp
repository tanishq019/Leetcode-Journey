class Solution {
public:
    bool checkDivisibility(int n) {
        int original = n;
        int summ = 0;
        int prod = 1;
        while (n > 0){
            int last_digit = n % 10;
            summ += last_digit;
            prod *= last_digit;
            n /= 10;
        }
        return original % (summ + prod) == 0;
    }
};