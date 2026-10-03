class Solution:
    def longestValidParentheses(self, s):

        max_length = 0

        balance = 0
        left_boundary = -1

        for i in range(len(s)):

            if balance < 0:
                balance = 0
                left_boundary = i - 1

            if s[i] == '(':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                current_length = i - left_boundary
                max_length = max(max_length, current_length)

        balance = 0
        right_boundary = len(s)

        for i in range(len(s)-1, -1, -1):

            if balance < 0:
                balance = 0
                right_boundary = i + 1

            if s[i] == ')':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                current_length = right_boundary - i
                max_length = max(max_length, current_length)

        return max_length