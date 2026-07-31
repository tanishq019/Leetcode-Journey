class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord("a")] += 1

        freq.sort(reverse = True)

        total_pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break

            presses = (i // 8) + 1
            total_pushes += freq[i] * presses

        return total_pushes