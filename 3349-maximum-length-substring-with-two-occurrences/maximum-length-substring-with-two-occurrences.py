class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            while count[s[i]] > 2:
                count[s[left]]-= 1
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len